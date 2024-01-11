# Generated by Django 5.0.1 on 2024-01-11 16:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0004_room_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WallFinish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_code', models.CharField(unique=True)),
                ('spec_code_suffix', models.CharField(unique=True)),
                ('spec_title', models.CharField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_walls', to=settings.AUTH_USER_MODEL)),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallFinishes', to='rooms.room')),
            ],
        ),
    ]
