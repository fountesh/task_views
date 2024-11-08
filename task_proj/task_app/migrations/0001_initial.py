# Generated by Django 5.1 on 2024-10-27 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('done', 'Done')], max_length=255)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('mid', 'Mid'), ('high', 'High')], max_length=10)),
                ('deadline', models.DateTimeField(default=datetime.datetime(2024, 10, 27, 11, 34, 49, 355783, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]