# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roberts', '0004_auto_20170913_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='script',
            field=models.TextField(),
        ),
    ]