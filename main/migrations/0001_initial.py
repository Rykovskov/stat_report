# Generated by Django 4.1.6 on 2023-02-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_data', models.IntegerField(verbose_name='Номер данных')),
                ('zabbix_id', models.IntegerField(verbose_name='Номер в забиксе')),
                ('title', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
