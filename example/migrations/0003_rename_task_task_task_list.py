# Generated by Django 5.0.4 on 2024-06-06 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_task_task'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='task_task',
            new_name='task_list',
        ),
    ]