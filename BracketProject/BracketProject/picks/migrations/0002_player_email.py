# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='email',
            field=models.EmailField(default='hi', max_length=254),
            preserve_default=False,
        ),
    ]
