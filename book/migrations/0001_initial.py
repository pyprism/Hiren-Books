# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('slug', models.CharField(unique=True, max_length=150)),
                ('note', models.TextField()),
                ('page_no', models.IntegerField(default=0)),
                ('pdf', models.FileField(upload_to='%d/%m/%Y')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
