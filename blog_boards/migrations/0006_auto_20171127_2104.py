# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_boards', '0005_auto_20171127_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_boards',
            old_name='sub_title',
            new_name='title',
        ),
    ]
