# Generated by Django 4.1.2 on 2022-11-15 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_sender', '0004_alter_client_timezone_alter_dispatch_filtr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='operator_code',
            field=models.CharField(max_length=3, verbose_name='Оператор клиента'),
        ),
        migrations.AlterField(
            model_name='dispatch',
            name='filtr',
            field=models.CharField(choices=[('По оператору', 'По оператору'), ('По тегу', 'По тегу')], max_length=32, verbose_name='Фильтр рассылки'),
        ),
        migrations.AlterField(
            model_name='message',
            name='send_dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 11, 12, 25, 701263, tzinfo=datetime.timezone.utc), verbose_name='Дата и время отправки'),
        ),
    ]