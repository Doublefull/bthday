# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 18:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0002_birthdays2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Birthdays2',
        ),
    ]