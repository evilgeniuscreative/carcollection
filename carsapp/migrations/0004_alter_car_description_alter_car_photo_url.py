# Generated by Django 5.0.1 on 2024-01-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0003_car_color_car_trim_car_year_alter_car_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='photo_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
