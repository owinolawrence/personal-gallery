# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-16 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20191216_0933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='category',
            new_name='category_item',
        ),
    ]
