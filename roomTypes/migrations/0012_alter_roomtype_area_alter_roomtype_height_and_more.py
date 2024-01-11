# Generated by Django 5.0.1 on 2024-01-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomTypes', '0011_roomtype_rooms_alter_roomtype_ffes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='area',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='room_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
