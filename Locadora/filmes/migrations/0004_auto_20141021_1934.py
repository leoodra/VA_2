# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0003_auto_20141020_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Preco', models.DecimalField(unique=True, null=True, verbose_name=b'Pre\xc3\xa7o', max_digits=4, decimal_places=2)),
                ('Categ', models.CharField(max_length=1, unique=True, null=True, verbose_name=b'Categoria', choices=[(b'1', b'Lan\xc3\xa7amento'), (b'2', b'Promo\xc3\xa7\xc3\xa3o'), (b'3', b'Normal')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='DtAlgd',
            field=models.DateField(null=True, verbose_name=b'Data Devolu\xc3\xa7\xc3\xa3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='DtAlg',
            field=models.DateField(null=True, verbose_name=b'Data Aluguel'),
        ),
        migrations.AlterField(
            model_name='cadfilme',
            name='Nome',
            field=models.CharField(max_length=100, unique=True, null=True, verbose_name=b'Nome'),
        ),
    ]
