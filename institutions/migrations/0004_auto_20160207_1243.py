# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0003_auto_20160206_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='citable_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
