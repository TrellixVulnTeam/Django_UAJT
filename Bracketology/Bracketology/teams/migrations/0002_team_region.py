# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='region',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
