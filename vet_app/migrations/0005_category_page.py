# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0004_auto_20141108_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('is_section', models.BooleanField(default=False, verbose_name='sezione')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorie',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('category', models.ForeignKey(to='vet_app.Category')),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Pagine',
            },
            bases=(models.Model,),
        ),
    ]
