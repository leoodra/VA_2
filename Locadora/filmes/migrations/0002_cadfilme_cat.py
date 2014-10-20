# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadfilme',
            name='Cat',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Categoria', choices=[(b'1', b'Lan\xc3\xa7amento'), (b'2', b'Promo\xc3\xa7\xc3\xa3o'), (b'3', b'Normal')]),
            preserve_default=True,
        ),
    ]
