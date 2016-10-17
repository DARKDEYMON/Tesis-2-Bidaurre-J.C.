# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0021_salidamaquinaria_equipo'),
        ('seguimiento', '0017_peticion_herramientas'),
    ]

    operations = [
        migrations.CreateModel(
            name='peticion_maquinaria_equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('petion_de_planificacion', models.BooleanField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.item')),
                ('maquinaria_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacenes.maquinaria_equipo')),
            ],
        ),
        migrations.AddField(
            model_name='peticion_herramientas',
            name='petion_de_planificacion',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peticion_insumos',
            name='petion_de_planificacion',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peticion_materiales',
            name='petion_de_planificacion',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
