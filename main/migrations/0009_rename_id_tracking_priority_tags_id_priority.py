# Generated by Django 4.1.6 on 2023-02-10 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_id_role_infrastructure_sp_id_infra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='priority_tags',
            old_name='id_tracking',
            new_name='id_priority',
        ),
    ]
