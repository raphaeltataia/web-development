# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('nome', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=35)),
                ('complemento', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('renda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Contato',
        ),
    ]
