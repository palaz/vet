# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0006_auto_20141108_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='categoria'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=100, default='pagina'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(to='vet_app.Category', verbose_name='Categoria'),
            preserve_default=True,
        ),
    ]
