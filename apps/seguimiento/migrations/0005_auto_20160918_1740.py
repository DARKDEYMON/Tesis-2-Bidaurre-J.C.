# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 21:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0004_auto_20160918_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='proyecto_fk',
            new_name='proyecto',
        ),
    ]
