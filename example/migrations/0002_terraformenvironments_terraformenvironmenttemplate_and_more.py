# Generated by Django 5.0.4 on 2024-06-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TerraformEnvironments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloud', models.CharField(max_length=100)),
                ('project', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('backend_object_type', models.CharField(max_length=100)),
                ('backend_object_name', models.CharField(max_length=100)),
                ('template_id', models.CharField(max_length=100)),
                ('env_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TerraformEnvironmentTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_context', models.TextField()),
                ('file_name', models.CharField(max_length=100)),
                ('template_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='terraformcodetemplate',
            old_name='file_name',
            new_name='env_id',
        ),
        migrations.RenameField(
            model_name='terraformcodetemplate',
            old_name='product_name',
            new_name='module_name',
        ),
    ]
