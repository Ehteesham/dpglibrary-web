# Generated by Django 4.1.3 on 2023-01-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpg', '0002_alter_contact_con_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ml_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ml_title', models.CharField(max_length=60)),
                ('ml_desc', models.CharField(max_length=500)),
                ('ml_img', models.ImageField(default='', upload_to='dpg/images')),
                ('ml_link', models.CharField(max_length=600)),
            ],
        ),
    ]
