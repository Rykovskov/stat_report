# Generated by Django 4.1.6 on 2023-02-10 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_priority_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infrastructure_sp',
            old_name='id_role',
            new_name='id_infra',
        ),
    ]
