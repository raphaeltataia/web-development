# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('cnpj', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=35)),
                ('complemento', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
                ('telefone', models.CharField(max_length=15)),
                ('responsavel', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=80)),
            ],
        ),
    ]