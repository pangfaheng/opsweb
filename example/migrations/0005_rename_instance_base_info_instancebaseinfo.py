# Generated by Django 5.0.4 on 2024-06-06 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_rename_task_list_tasklist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='instance_base_info',
            new_name='InstanceBaseInfo',
        ),
    ]