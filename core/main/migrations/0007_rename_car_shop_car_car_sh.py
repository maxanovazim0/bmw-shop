# Generated by Django 5.0.6 on 2024-07-02 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_cars_car_rename_car_detail_car_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_shop',
            new_name='car_sh',
        ),
    ]
