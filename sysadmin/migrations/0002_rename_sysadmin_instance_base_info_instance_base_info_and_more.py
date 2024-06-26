# Generated by Django 5.0.4 on 2024-05-09 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysadmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sysadmin_instance_base_info',
            new_name='instance_base_info',
        ),
        migrations.RenameModel(
            old_name='sysadmin_instance_cloud_info',
            new_name='instance_cloud_info',
        ),
        migrations.RenameModel(
            old_name='sysadmin_instance_connect_info',
            new_name='instance_connect_info',
        ),
        migrations.RenameModel(
            old_name='sysadmin_instance_data_disk_info',
            new_name='instance_data_disk_info',
        ),
        migrations.RenameModel(
            old_name='sysadmin_instance_tags_info',
            new_name='instance_tags_info',
        ),
        migrations.RenameIndex(
            model_name='instance_cloud_info',
            new_name='sysadmin_in_cloud_i_d48184_idx',
            old_name='sysadmin_sy_cloud_i_437c46_idx',
        ),
        migrations.RenameIndex(
            model_name='instance_connect_info',
            new_name='sysadmin_in_instanc_186c57_idx',
            old_name='sysadmin_sy_instanc_6591e0_idx',
        ),
        migrations.RenameIndex(
            model_name='instance_data_disk_info',
            new_name='sysadmin_in_instanc_7e4b7b_idx',
            old_name='sysadmin_sy_instanc_580546_idx',
        ),
        migrations.RenameIndex(
            model_name='instance_tags_info',
            new_name='sysadmin_in_instanc_26d542_idx',
            old_name='sysadmin_sy_instanc_76d051_idx',
        ),
    ]
