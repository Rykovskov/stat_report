from main.applogic import *
from main.models import History
from main.models import Trcking_tags
import datetime
import json

#Delete all records from History
#print('Производим очистку базы')
#del_all_History = History.objects.all()
#del_all_History.delete()


startdate = datetime.date(1970,1,1)
Trcking_tags_table = Trcking_tags.objects.all()
#Обновление статистики в БД
#Удаляем старые данные
dt_now = datetime.datetime.now()
enddate = yearsago(1, dt_now)
del_History = History.objects.filter(dt_zap__range=[startdate, enddate])
print('Start date:', startdate, ' End date: ', enddate)
del_History.delete()

#Добавляем актуальные записи
host_sp = get_zabbix_host_by_tags(Trcking_tags_table)
for h in host_sp:
    d_h = json.loads(str(h).replace("'", '"'))
    if d_h['tags'][-1]['tag'] == 'Critical_Parameters':
        cr_par = d_h['tags'][-1]['value']
        host_par = str(cr_par).split(';')
    else:
        host_par = []
    host_items_data_save(h['hostid'], h['name'], host_par)