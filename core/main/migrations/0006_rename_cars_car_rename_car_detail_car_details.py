# Generated by Django 5.0.6 on 2024-07-02 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_biz_haqmizda_biz_haqmizda_ga_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cars',
            new_name='car',
        ),
        migrations.RenameModel(
            old_name='car_detail',
            new_name='car_details',
        ),
    ]
