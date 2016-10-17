# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 20:07
from __future__ import unicode_literals

import apps.seguimiento.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0018_auto_20161014_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='reporte_fotografico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum', models.FileField(blank=True, null=True, upload_to='reporte_fotos/', validators=[apps.seguimiento.models.validate_file_extension])),
            ],
        ),
        migrations.CreateModel(
            name='reportes_avance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alto', models.FloatField(default=0.0)),
                ('largo', models.FloatField(default=0.0)),
                ('ancho', models.FloatField(default=0.0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.item')),
            ],
        ),
        migrations.AddField(
            model_name='reporte_fotografico',
            name='reportes_avance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.reportes_avance'),
        ),
    ]
