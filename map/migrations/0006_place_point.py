# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 14:16
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_place_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
