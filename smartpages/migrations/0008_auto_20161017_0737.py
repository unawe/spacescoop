# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import now


class Migration(migrations.Migration):

    dependencies = [
        ('smartpages', '0007_auto_20160201_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartpage',
            name='embargo_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='smartpage',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='smartpage',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='smartpage',
            name='release_date',
            field=models.DateTimeField(default=now()),
            preserve_default=False,
        ),
    ]
