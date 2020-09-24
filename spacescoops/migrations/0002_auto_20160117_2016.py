# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spacescoops', '0001_squashed_0040_auto_20160109_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='title', always_update=True, max_length=200, editable=False),
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, max_length=200, populate_from='title', editable=False, unique_with=('language_code',)),
        ),
    ]
