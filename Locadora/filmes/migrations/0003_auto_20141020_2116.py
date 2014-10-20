# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('filmes', '0002_cadfilme_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DtAlg', models.DateField(null=True, verbose_name=b'Data Devolu\xc3\xa7\xc3\xa3o')),
                ('FilAlg', models.ForeignKey(verbose_name=b'Nome do Filme', to='filmes.Cadfilme', null=True)),
                ('PesAlg', models.ForeignKey(verbose_name=b'Pessoa do Aluguel', to='cliente.Pessoa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='cadfilme',
            name='DtLan',
            field=models.DateField(null=True, verbose_name=b'Data de Lan\xc3\xa7amento'),
        ),
    ]
