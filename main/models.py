from django.db import models


# Create your models here.
class History(models.Model):
    zabbix_id = models.IntegerField('Номер в забиксе')
    dt_zap = models.DateField('Дата записи', null=True)
    zabbix_value_name_host = models.CharField('Имя хоста',default='',max_length=50, null=True)
    zabbix_value_cur = models.CharField('Текущее значение параметра',default='',max_length=150, null=True)
    zabbix_value_avg_dey = models.CharField('Среднее значение параметра за день', default='', max_length=150,null=True)
    zabbix_value_avg_week = models.CharField('Среднее значение параметра за неделю',default='',max_length=150, null=True)
    zabbix_value_avg_month = models.CharField('Среднее значение параметра за месяц',default='',max_length=150, null=True)
    zabbix_value_avg_year = models.CharField('Среднее значение параметра за год',default='',max_length=150, null=True)
    zabbix_value_deviation_day = models.CharField('Отклонеие параметра от вчерашнего',default='',max_length=150, null=True)
    zabbix_value_deviation_week = models.CharField('Отклонеие параметра от недельного',default='',max_length=150, null=True)
    zabbix_value_deviation_month = models.CharField('Отклонеие параметра от месячного',default='',max_length=150, null=True)
    zabbix_value_deviation_year = models.CharField('Отклонеие параметра от годового',default='',max_length=150, null=True)
    zabbix_value_trend = models.ImageField('Тренд',default='',max_length=150, null=True)
    title = models.CharField('Описание параметра',default='',max_length=150, null=True)

    def __str__(self):
        return self.title


class approle_parametrs(models.Model):
    approle = models.ForeignKey('Roles_sp', on_delete=models.PROTECT, null=False)
    name_parametr = models.CharField('Наименование параметра',default='',max_length=150, null=False)

    def __str__(self):
        return self.name_parametr
    class Meta:
        verbose_name = 'Параметры ролей'

class Trcking_tags(models.Model):
    infrastructure_tag = models.ForeignKey('Infrastructure_sp', on_delete= models.PROTECT, null=True)
    service_tag = models.ForeignKey('Services_sp', on_delete= models.PROTECT, null=True)
    #role_tag = models.ForeignKey('Roles_sp', on_delete= models.PROTECT, null=True)
    priority_tag = models.ForeignKey('Priority_tags', on_delete= models.PROTECT, null=True)
    descr_track = models.CharField('Примечание',default='',max_length=150, null=True)

    def __str__(self):
        return self.descr_track

    class Meta:
        verbose_name = 'Текущая настройка'


class Report_tags(models.Model):
    tags = models.CharField('Тег в забиксе',default='',max_length=150)
    title = models.CharField('Описание тега',default='',max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег для отчетов'


class Values_tags(models.Model):
    tags_value = models.CharField('Значение тега в забиксе',default='',max_length=150, db_index=True)

    def __str__(self):
        return self.tags_value

    class Meta:
        verbose_name = 'Содержание тега'

class Services_sp(models.Model):
    title = models.CharField('Название сервиса',default='',max_length=150, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список сервисов'

class Roles_sp(models.Model):
    title = models.CharField('Название роли',default='',max_length=150, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список ролей'

class Infrastructure_sp(models.Model):
    title = models.CharField('Инфроструктура',default='',max_length=150, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список инфраструктур'


class Priority_tags(models.Model):
    title = models.CharField('Приоритет',default='',max_length=150, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Приоритеты'