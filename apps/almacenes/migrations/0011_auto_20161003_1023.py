# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 14:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0010_auto_20161003_1022'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='herramientasalmacen',
            unique_together=set([('almacen', 'herramientas')]),
        ),
    ]
