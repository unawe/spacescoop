# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartpages', '0002_smartpage_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartpage',
            name='code',
            field=models.CharField(db_index=True, max_length=100, blank=True),
        ),
    ]
