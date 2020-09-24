# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spacescoops', '0007_auto_20160201_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalNewsSource',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200, help_text='Short (and commonly used) name')),
                ('slug', models.SlugField(max_length=200, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.')),
                ('fullname', models.CharField(blank=True, max_length=200, help_text='If set, the full name will be used in some places instead of the name')),
                ('url', models.CharField(max_length=255)),
                ('logo', sorl.thumbnail.fields.ImageField(upload_to='partners', blank=True, null=True)),
                ('article_count', models.IntegerField(default=0, editable=False)),
            ],
            options={
                'verbose_name': 'partner',
            },
        ),
        migrations.CreateModel(
            name='OriginalNewsSourceTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('language_code', models.CharField(db_index=True, verbose_name='Language', max_length=15)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, help_text='Text to appear in Parnet page')),
                ('master', models.ForeignKey(to='spacescoops.OriginalNewsSource', related_name='translations', null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'partner translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='originalnewssourcetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
