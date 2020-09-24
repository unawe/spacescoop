# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartpages', '0006_smartembed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smartembed',
            options={'ordering': ('code',), 'verbose_name': 'embed'},
        ),
        migrations.AlterField(
            model_name='smartembed',
            name='code',
            field=models.CharField(db_index=True, blank=True, help_text='Internal code to identify the embed; if set, do not modify. When in doubt, leave empty.', unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='smartpage',
            name='code',
            field=models.CharField(db_index=True, blank=True, help_text='Internal code to identify the page; if set, do not modify. When in doubt, leave empty.', unique=True, max_length=100),
        ),
    ]
