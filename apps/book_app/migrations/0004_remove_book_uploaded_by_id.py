# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 00:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_book_uploader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='uploaded_by_id',
        ),
    ]