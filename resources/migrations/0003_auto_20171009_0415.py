# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 04:15
from __future__ import unicode_literals

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_photo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
        migrations.AddField(
            model_name='photo',
            name='image_url',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
    ]
