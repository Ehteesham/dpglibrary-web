# Generated by Django 4.1.3 on 2023-01-29 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpg', '0006_alter_ml_list_ml_sno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ml_list',
            name='ml_sno',
        ),
    ]
