# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160623_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='total_years',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
