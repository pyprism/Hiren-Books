# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20151006_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='date',
            new_name='added_at',
        ),
        migrations.AddField(
            model_name='book',
            name='finished_at',
            field=models.DateField(default=datetime.datetime(2015, 10, 7, 15, 8, 16, 873524, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
