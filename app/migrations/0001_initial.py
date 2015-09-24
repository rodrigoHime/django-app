# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name='N\xfamero')),
                ('text', models.CharField(max_length=255, verbose_name='Texto', db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255, verbose_name=b'Log')),
                ('type', models.IntegerField(default=1, choices=[(1, b'Cadastro'), (2, b'Atualiza\xc3\xa7\xc3\xa3o'), (3, b'Dele\xc3\xa7\xc3\xa3o')])),
                ('datetime', models.DateTimeField(verbose_name=b'Data de Cria\xc3\xa7\xc3\xa3o')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
