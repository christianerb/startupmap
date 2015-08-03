# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, blank=True),
        ),
    ]
