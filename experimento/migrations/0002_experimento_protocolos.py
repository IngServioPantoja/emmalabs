# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0002_remove_protocolo_experimentos'),
        ('experimento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experimento',
            name='protocolos',
            field=models.ManyToManyField(null=True, to='protocolo.Protocolo'),
        ),
    ]
