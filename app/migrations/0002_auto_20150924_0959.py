# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Data de Cria\xc3\xa7\xc3\xa3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='log',
            name='type',
            field=models.IntegerField(default=1, choices=[(1, b'Cria\xc3\xa7\xc3\xa3o'), (2, b'Atualiza\xc3\xa7\xc3\xa3o'), (3, b'Dele\xc3\xa7\xc3\xa3o')]),
            preserve_default=True,
        ),
    ]
