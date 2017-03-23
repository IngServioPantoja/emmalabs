# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0002_auto_20170320_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='asistente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asistente', to='usuario.Usuario'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='cientifico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cientifico', to='usuario.Usuario'),
        ),
    ]
