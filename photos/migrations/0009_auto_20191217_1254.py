# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-17 09:54
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_auto_20191216_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
