# Generated by Django 3.0.2 on 2020-02-21 09:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20200221_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='college',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='whatsapp_number',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator('^[6-9]{1}[0-9]{9}$')]),
        ),
    ]
