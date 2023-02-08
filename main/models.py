from django.db import models

# Create your models here.
class history(models.Model):
    id_data = models.IntegerField('Номер данных')
    zabbix_id = models.IntegerField('Номер в забиксе')
    title = models.TextField('Описание')

    def __str__(self):
        return self.title
