# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='CPF',
            field=models.CharField(max_length=14, unique=True, null=True, verbose_name=b'CPF'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='Sexo',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='Nome',
            field=models.CharField(max_length=100, unique=True, null=True, verbose_name=b'Nome'),
        ),
    ]
