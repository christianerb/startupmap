# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_startup_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='category',
            field=models.IntegerField(null=True, choices=[(0, b'Startup'), (1, b'Investor'), (2, b'Other')]),
        ),
    ]
