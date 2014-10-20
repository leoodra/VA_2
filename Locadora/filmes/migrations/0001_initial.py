# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadfilme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('DtLan', models.DateField(null=True, verbose_name=b'Data deLan\xc3\xa7amento')),
                ('Nomed', models.CharField(max_length=100, null=True, verbose_name=b'Nome Diretor')),
                ('Gen', models.CharField(max_length=1, null=True, verbose_name=b'G\xc3\xaanero', choices=[(b'1', b'A\xc3\xa7\xc3\xa3o'), (b'2', b'Aventura'), (b'3', b'Com\xc3\xa9dia'), (b'4', b'Drama'), (b'5', b'Document\xc3\xa1rio'), (b'6', b'Policial'), (b'7', b'Romance'), (b'8', b'Terror'), (b'9', b'Suspense')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
