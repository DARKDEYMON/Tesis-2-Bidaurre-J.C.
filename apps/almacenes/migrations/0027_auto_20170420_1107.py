# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-20 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0026_auto_20170322_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresoinsumos',
            name='no_factura',
            field=models.PositiveIntegerField(default=123456789),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingresomaterial',
            name='no_factura',
            field=models.PositiveIntegerField(default=123456789),
            preserve_default=False,
        ),
    ]
