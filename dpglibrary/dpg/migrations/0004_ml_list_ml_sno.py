# Generated by Django 4.1.3 on 2023-01-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpg', '0003_ml_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='ml_list',
            name='ml_sno',
            field=models.IntegerField(default=0),
        ),
    ]
