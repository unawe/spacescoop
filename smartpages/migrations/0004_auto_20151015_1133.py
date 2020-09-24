# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartpages', '0003_auto_20151014_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smartpage',
            options={'verbose_name': 'page'},
        ),
        migrations.AlterField(
            model_name='smartpage',
            name='code',
            field=models.CharField(blank=True, max_length=100, db_index=True, help_text='Optional; if in doubt, leave empty.'),
        ),
        migrations.AlterField(
            model_name='smartpagetranslation',
            name='url',
            field=models.CharField(verbose_name='URL', help_text='Example: "/about/contact/". Make sure to have leading and trailing slashes.', max_length=100, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='smartpagetranslation',
            unique_together=set([('language_code', 'url'), ('language_code', 'master')]),
        ),
    ]
