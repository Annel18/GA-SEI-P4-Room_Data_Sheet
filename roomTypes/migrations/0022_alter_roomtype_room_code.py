# Generated by Django 5.0.1 on 2024-01-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomTypes', '0021_alter_roomtype_room_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='room_code',
            field=models.CharField(unique=True),
        ),
    ]
