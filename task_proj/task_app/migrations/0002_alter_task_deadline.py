# Generated by Django 5.1 on 2024-10-27 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 27, 11, 59, 46, 862225, tzinfo=datetime.timezone.utc)),
        ),
    ]
