# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20171012_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='bad_avaliations',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='good_avaliations',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
