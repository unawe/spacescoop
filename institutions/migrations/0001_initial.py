# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('citable_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=255, help_text='Short (and commonly used) name')),
                ('slug', models.SlugField(unique=True, max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.')),
                ('fullname', models.CharField(help_text='If set, the full name will be used in some places instead of the name', max_length=255, blank=True)),
                ('url', models.URLField(null=True, max_length=255, blank=True)),
                ('country', models.CharField(max_length=255, blank=True)),
                ('logo', sorl.thumbnail.fields.ImageField(null=True, upload_to='institutions', blank=True)),
                ('spacescoop_count', models.IntegerField(editable=False, default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='InstitutionTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', ckeditor.fields.RichTextField(help_text='Text to appear in Institution page', null=True, blank=True)),
                ('master', models.ForeignKey(to='institutions.Institution', related_name='translations', null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'institution translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='institutiontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
