# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20151009_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='hiren/%Y/%m/%d'),
        ),
    ]