# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experimento', '0002_experimento_protocolos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimento',
            name='protocolos',
            field=models.ManyToManyField(to='protocolo.Protocolo'),
        ),
    ]
