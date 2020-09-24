# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0005_auto_20160211_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='institution',
            field=models.ForeignKey(blank=True, to='institutions.Institution', null=True, on_delete=models.CASCADE),
        ),
    ]
