# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacescoops', '0003_article_spaceawe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='spaceawe_category',
            field=models.CharField(choices=[('space', 'Space Exploration'), ('planet', 'Earth Observation'), ('nav', 'Navigation'), ('herit', 'Islamic heritage')], max_length=20, blank=True),
        ),
    ]
