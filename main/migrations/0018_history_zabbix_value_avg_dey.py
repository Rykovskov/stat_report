# Generated by Django 4.1.6 on 2023-03-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_rename_dt_history_dt_zap'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='zabbix_value_avg_dey',
            field=models.CharField(default='', max_length=150, null=True, verbose_name='Среднее значение параметра за день'),
        ),
    ]