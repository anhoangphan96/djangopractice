# Generated by Django 4.2.6 on 2023-10-19 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_create_date_post_created_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 19, 2, 25, 14, 491805, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 19, 2, 25, 14, 491805, tzinfo=datetime.timezone.utc)),
        ),
    ]
