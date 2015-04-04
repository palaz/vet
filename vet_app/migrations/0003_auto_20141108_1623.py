# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0002_auto_20141108_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_section',
            field=models.BooleanField(verbose_name='sezione', default=False),
            preserve_default=True,
        ),
    ]
