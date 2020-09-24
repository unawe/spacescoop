# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacescoops', '0006_auto_20160126_2201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-release_date'], 'verbose_name': 'space scoop'},
        ),
    ]
