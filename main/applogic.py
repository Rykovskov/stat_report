from pyzabbix import ZabbixAPI
import pandas as pd
import time
import datetime
import sys
from .models import History
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def yearsago(years, from_date=None):
    if from_date is None:
        from_date = datetime.now()
    return from_date - relativedelta(years=years)


def get_history_val(period, id_item, conn_zabix):
    t_from=1000000
    if period== 'YEAR':
        one_year = yearsago(1, datetime.datetime.now())
        two_year = yearsago(2, datetime.datetime.now())
        # t_from = time.mktime(datetime.datetime.strptime('2023-03-10 08:00:00', "%Y-%m-%d %H:%M:%S").timetuple())
        t_from = int(time.mktime(two_year.timetuple()))
        t_till = int(time.mktime(one_year.timetuple()))
    if period== 'MONTH':
        dt = datetime.datetime.now()- relativedelta(months=-2)
        t_from = int(time.mktime(dt.timetuple()))
        dt = datetime.datetime.now() - relativedelta(months=-1)
        t_till = int(time.mktime(dt.timetuple()))
    if period=='WEEK':
        dt = datetime.datetime.now() -timedelta(weeks=2)
        t_from = int(time.mktime(dt.timetuple()))
        dt = datetime.datetime.now() - timedelta(weeks=1)
        t_till = int(time.mktime(dt.timetuple()))
    if period=='DAY':
        dt = datetime.datetime.now() -timedelta(days=2)
        t_from = int(time.mktime(dt.timetuple()))
        dt = datetime.datetime.now() - timedelta(days=1)
        t_till = int(time.mktime(dt.timetuple()))
    res = conn_zabix.trend.get(itemids=id_item, output=['value_avg'], time_till=t_till, time_from=t_from, limit=1)
    if len(res)>0:
        return res[0]['value_avg']
    else:
        return None


def connect_zabbix():
    return ZabbixAPI('http://10.200.10.14', user='report_web', password='tv60hu02')


def delete_old_stat(zabbic_conn, dt_delete):
    #Удаление старых данных
    if type(dt_delete)=='datetime.datetime':
        res = History.objects.filter(dt_zap < dt_delete)
        res.delete()
        return True
    else:
        return False


def get_data_from_history_by_dt(id_request, dt_request, name_field):
    #print('--------------------DATE--------------')
    #print(dt_request)
    befor_History_recod = History.objects.filter(zabbix_id=int(id_request)) & History.objects.filter(
        dt_zap__year=dt_request.year,
        dt_zap__month=dt_request.month,
        dt_zap__day=dt_request.day)
    #print('--------------------------------------')
    if len(befor_History_recod) > 0:
        last_r = befor_History_recod.last()
        return getattr(last_r, name_field)
    else:
        return None


def get_zabbix_host_by_tags(sp_tags):
    z = connect_zabbix()
    answer = z.do_request('apiinfo.version')
    #Формируем список тегов для запроса в заббикс
    t_query=[]
    for t in sp_tags:
        d={}
        d1={}
        d2={}
        d['tag'] = 'Infrastructure'
        d['value'] = str(t.infrastructure_tag)
        d['operator'] = 1
        t_query.append(d)
        d1['tag'] = 'AppService'
        d1['value'] = str(t.service_tag)
        d1['operator'] = 1
        t_query.append(d1)
        d2['tag'] = 'Priority'
        d2['value'] = str(t.priority_tag)
        d2['operator'] = 1
        t_query.append(d2)
    t_query1 = pd.DataFrame(t_query).drop_duplicates().to_dict('records')
    sp_hosts = z.do_request('host.get', {'selectTags': 'extend', 'output': ['hostid', 'name'], 'tags': t_query1})
    res = sp_hosts['result']
    return res

def host_items_data_save(hostid, host_name, items_names):
    #Получение данных о хосте
    z = connect_zabbix()
    if len(items_names)>0:
        for items_name in items_names:
            # Заполняем таблицу истории
            items = z.do_request('item.get', {'hostids': [hostid], 'output': ["itemids", "name", "lastvalue"],
                                              'search': {'name': items_name}})
            for i in items['result']:
                item_id = i['itemid']
                item_name = i['name']
                item_cur_val = i['lastvalue']
                #print('item_cur_val - ', item_cur_val)
                #Среднее значение параметра за прошедший год
                year_val = get_history_val('YEAR', item_id, z)
                # Получаем этот параметры каким он был год назад yearsago(1, datetime.datetime.now())
                befor_year_val = get_data_from_history_by_dt(item_id,
                                                             yearsago(1, datetime.datetime.now()),
                                                             'zabbix_value_avg_year')
                if type(befor_year_val)=='int' or type(befor_year_val)=='float':
                    deviation_year = befor_year_val - year_val
                else:
                    deviation_year = None
                #Среднее значение параметра за прошедший месяц
                month_val = get_history_val('MONTH', item_id, z)
                befor_month_val = get_data_from_history_by_dt(item_id,
                                                              (datetime.datetime.now() - relativedelta(months=-1)),
                                                              'zabbix_value_avg_month')
                if type(befor_month_val) == 'int' or type(befor_month_val) == 'float':
                    #print('FLOAT------------------------------------------------', befor_month_val)
                    deviation_month = befor_month_val - month_val
                else:
                    deviation_month = None
                #Среднее значение параметра за прошедшую неделю
                week_val = get_history_val('WEEK', item_id, z)
                befor_week_val = get_data_from_history_by_dt(item_id,
                                                              (datetime.datetime.now() -timedelta(weeks=-1)),
                                                              'zabbix_value_avg_week')
                if type(befor_week_val) == 'int' or type(befor_week_val) == 'float':
                    #print('FLOAT------------------------------------------------', befor_week_val)
                    deviation_week = befor_week_val - week_val
                else:
                    #print('NOT FLOAT', befor_week_val)
                    deviation_week = None
                # Среднее значение параметра за прошедшую день
                dey_val = get_history_val('DAY', item_id, z)
                befor_dey_val = get_data_from_history_by_dt(item_id,
                                                              (datetime.datetime.now() -timedelta(days=-1)),
                                                              'zabbix_value_avg_dey')
                if type(befor_dey_val) == 'int' or type(befor_dey_val) == 'float':
                    print('FLOAT------------------------------------------------', befor_dey_val)
                    deviation_day = befor_dey_val - dey_val
                else:
                    deviation_day = None
                #Добавляем новую запись в таблицу истории
                new_history = History()
                new_history.zabbix_id = int(item_id)
                new_history.dt_zap = datetime.datetime.now() + timedelta(days=2)
                new_history.zabbix_value_name_host = host_name
                new_history.zabbix_value_cur = item_cur_val
                new_history.zabbix_value_avg_dey = dey_val
                new_history.zabbix_value_avg_week = week_val
                new_history.zabbix_value_deviation_month = month_val
                new_history.zabbix_value_avg_year = year_val
                new_history.zabbix_value_deviation_year = deviation_year
                new_history.zabbix_value_deviation_month = deviation_month
                new_history.zabbix_value_deviation_week = deviation_week
                new_history.zabbix_value_deviation_day = deviation_day
                new_history.title = item_name
                #Сохроаняем
                new_history.save()
    return True

