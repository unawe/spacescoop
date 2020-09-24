# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartpage',
            name='code',
            field=models.CharField(db_index=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]
