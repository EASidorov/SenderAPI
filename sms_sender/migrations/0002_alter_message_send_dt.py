# Generated by Django 4.1.2 on 2022-11-15 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_sender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='send_dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 10, 18, 51, 548393, tzinfo=datetime.timezone.utc), verbose_name='Дата и время отправки'),
        ),
    ]
