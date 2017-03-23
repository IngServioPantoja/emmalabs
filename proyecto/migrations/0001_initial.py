# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('experimento', '0002_experimento_protocolos'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('asistentes', models.ManyToManyField(null=True, to='usuario.Usuario')),
                ('experimentos', models.ManyToManyField(null=True, to='experimento.Experimento')),
            ],
        ),
    ]
