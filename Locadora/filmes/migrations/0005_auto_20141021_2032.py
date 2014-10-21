# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0004_auto_20141021_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlugelFlmes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AlugelFlmes', models.ForeignKey(to='filmes.Aluguel', null=True)),
                ('FilAlg', models.ForeignKey(verbose_name=b'Nome do Filme', to='filmes.Cadfilme', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='aluguel',
            name='FilAlg',
        ),
    ]
