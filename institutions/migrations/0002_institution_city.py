# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='city',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
