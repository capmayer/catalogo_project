# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 18:44
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recourses', '0002_photos_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='recourse',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='ok', editable=False, populate_from='title'),
        ),
    ]
