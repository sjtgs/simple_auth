# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 20:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_boards', '0003_auto_20171127_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='text',
            new_name='title',
        ),
    ]
