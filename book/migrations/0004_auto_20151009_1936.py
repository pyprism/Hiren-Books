# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20151007_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='finished_at',
            field=models.DateField(null=True, blank=True),
        ),
    ]
