# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0027_auto_20161023_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiales_locales',
            name='unidad',
            field=models.CharField(default='cubos', max_length=10),
            preserve_default=False,
        ),
    ]
