# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacescoops', '0002_auto_20160117_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='spaceawe_category',
            field=models.CharField(blank=True, max_length=20, choices=[('space', 'Our wonderful Universe'), ('planet', 'Our fragile planet'), ('nav', 'Navigation through the ages'), ('herit', 'Islamic heritage')]),
        ),
    ]
