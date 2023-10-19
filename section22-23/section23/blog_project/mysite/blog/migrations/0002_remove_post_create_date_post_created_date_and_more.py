# Generated by Django 4.2.6 on 2023-10-19 02:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 19, 2, 24, 30, 411053, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 19, 2, 24, 30, 411053, tzinfo=datetime.timezone.utc)),
        ),
    ]