# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0005_category_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_section',
            field=models.BooleanField(default=False, verbose_name='Sezione'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='Nome', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(verbose_name='Titolo', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='text',
            field=models.TextField(verbose_name='Testo'),
            preserve_default=True,
        ),
    ]
