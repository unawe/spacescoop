# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacescoops', '0005_auto_20160124_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='spaceawe_category',
        ),
        migrations.AddField(
            model_name='article',
            name='earth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='heritage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='navigation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='space',
            field=models.BooleanField(default=False),
        ),
    ]
