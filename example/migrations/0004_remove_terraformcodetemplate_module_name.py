# Generated by Django 5.0.4 on 2024-06-13 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_remove_terraformcodetemplate_cloud_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terraformcodetemplate',
            name='module_name',
        ),
    ]
