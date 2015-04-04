# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0007_auto_20141109_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_section',
            field=models.BooleanField(verbose_name='Consigli Vet', default=False),
            preserve_default=True,
        ),
    ]
