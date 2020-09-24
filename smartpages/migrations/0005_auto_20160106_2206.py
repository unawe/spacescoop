# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartpages', '0004_auto_20151015_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smartpagetranslation',
            options={'verbose_name': 'page translation'},
        ),
        migrations.AlterField(
            model_name='smartpage',
            name='code',
            field=models.CharField(max_length=100, blank=True, help_text='Internal code to identify tha page; if set, do not modify. When in doubt, leave empty.', db_index=True),
        ),
    ]
