# Generated by Django 4.1.6 on 2023-02-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='report_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tags', models.IntegerField(verbose_name='Номер данных')),
                ('tags', models.TextField(verbose_name='Тег в забиксе')),
                ('title', models.TextField(verbose_name='Описание тега')),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='zabbix_value_avg_month',
            field=models.TextField(default='', verbose_name='Среднее значение параметра за месяц'),
        ),
        migrations.AddField(
            model_name='history',
            name='zabbix_value_avg_week',
            field=models.TextField(default='', verbose_name='Среднее значение параметра за неделю'),
        ),
        migrations.AddField(
            model_name='history',
            name='zabbix_value_avg_year',
            field=models.TextField(default='', verbose_name='Среднее значение параметра за год'),
        ),
        migrations.AddField(
            model_name='history',
            name='zabbix_value_cur',
            field=models.TextField(default='', verbose_name='Текущее значение параметра'),
        ),
        migrations.AddField(
            model_name='history',
            name='zabbix_value_deviation_day',
            field=models.TextField(default='', verbose_name='Отклонеие параметра от вчерашнего'),
        ),
        migrations.AddField(
            model_name='history',
            name='zabbix_value_deviation_month',
            field=models.TextField(default='', verbose_name='Отклонеие параметра от месячного'),
        ),
        migrations.AddField(
            model_name='history',
            name='zabbix_value_deviation_week',
            field=models.TextField(default='', verbose_name='Отклонеие параметра от недельного'),
        ),
        migrations.AddField(
            model_name='history',
            name='zabbix_value_deviation_year',
            field=models.TextField(default='', verbose_name='Отклонеие параметра от годового'),
        ),
        migrations.AddField(
            model_name='history',
            name='zabbix_value_trend',
            field=models.ImageField(default='', upload_to='', verbose_name='Тренд'),
        ),
        migrations.AlterField(
            model_name='history',
            name='title',
            field=models.TextField(default='', verbose_name='Описание параметра'),
        ),
    ]