# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='EntryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('slug', autoslug.fields.AutoSlugField(max_length=200, always_update=True, populate_from='title', unique_with=('language_code',), editable=False)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('short_description', models.CharField(max_length=180)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('master', models.ForeignKey(related_name='translations', to='glossary.Entry', null=True, on_delete=models.CASCADE)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='entrytranslation',
            unique_together=set([('language_code', 'master'), ('language_code', 'slug')]),
        ),
    ]
