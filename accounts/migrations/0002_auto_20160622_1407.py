# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='male',
            new_name='is_male',
        ),
    ]
