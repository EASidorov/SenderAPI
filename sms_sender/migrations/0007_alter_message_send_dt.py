# Generated by Django 4.1.2 on 2022-11-15 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_sender', '0006_operator_tag_alter_client_tag_alter_message_send_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='send_dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 14, 39, 32, 343750, tzinfo=datetime.timezone.utc), verbose_name='Дата и время отправки'),
        ),
    ]
