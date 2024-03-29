# Generated by Django 4.1.6 on 2023-03-10 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_trcking_tags_role_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='zabbix_value_name_host',
            field=models.CharField(default='', max_length=50, verbose_name='Имя хоста'),
        ),
        migrations.CreateModel(
            name='approle_parametrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_parametr', models.CharField(default='', max_length=150, verbose_name='Наименование параметра')),
                ('approle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.roles_sp')),
            ],
            options={
                'verbose_name': 'Параметры ролей',
            },
        ),
    ]
