# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0006_auto_20161001_1823'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ingreso_material',
            unique_together=set([('almacen', 'material')]),
        ),
    ]
