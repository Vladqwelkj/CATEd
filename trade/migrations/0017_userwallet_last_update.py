# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0016_userwallet_total_usd'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwallet',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
