# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categorie', 'verbose_name': 'Categoria'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name_plural': 'Pagine', 'verbose_name': 'Pagina'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='isSection',
            new_name='is_section',
        ),
    ]
