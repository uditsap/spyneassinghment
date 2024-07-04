# Generated by Django 5.0.3 on 2024-07-04 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notification_service', '0001_initial'),
        ('user_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_service.user'),
        ),
    ]
