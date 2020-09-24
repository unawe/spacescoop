# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0002_institution_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='latitude',
            field=models.FloatField(null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='longitude',
            field=models.FloatField(null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='institution',
            field=models.ForeignKey(to='institutions.Institution', null=True, on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='person',
            name='spaceawe_partner',
            field=models.BooleanField(default=False),
        ),
    ]
