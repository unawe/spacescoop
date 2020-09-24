# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import spacescoops.models
import uuid
import taggit_autosuggest.managers
import autoslug.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(blank=True, null=True)),
                ('uuid', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(help_text='The 4 digit code that identifies the Article, in the format "YY##": year, folowed by sequential number.', db_index=True, max_length=4)),
            ],
            options={
                'ordering': ['-release_date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('language_code', models.CharField(verbose_name='Language', db_index=True, max_length=15)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', always_update=True)),
                ('title', models.CharField(verbose_name='title', max_length=200)),
                ('story', ckeditor.fields.RichTextField()),
                ('cool_fact', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('translation_credit_text', models.CharField(help_text='If set, this text will replace the default translation for credits.', blank=True, max_length=255, null=True)),
                ('translation_credit_url', models.CharField(blank=True, max_length=255, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modification_date', models.DateTimeField(auto_now=True, null=True)),
                ('master', models.ForeignKey(to='spacescoops.Article', null=True, related_name='translations', on_delete=models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('position', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('position',),
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('language_code', models.CharField(verbose_name='Language', db_index=True, max_length=15)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, always_update=True, populate_from='title', unique_with=('language_code',))),
                ('title', models.CharField(verbose_name='title', max_length=200)),
                ('master', models.ForeignKey(to='spacescoops.Category', null=True, related_name='translations', on_delete=models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('show', models.BooleanField(verbose_name='Show', help_text='Include in attachment list.', default=False)),
                ('position', models.PositiveSmallIntegerField(verbose_name='Position', help_text='Used to define the order of attachments in the attachment list.', default=0)),
                ('file', sorl.thumbnail.fields.ImageField(upload_to=spacescoops.models.get_file_path_article_attachment, blank=True, null=True)),
                ('hostmodel', models.ForeignKey(to='spacescoops.Article', related_name='images', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['position', 'id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OriginalNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('url', models.CharField(verbose_name='URL', max_length=255)),
                ('article', models.ForeignKey(to='spacescoops.Article', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'original news',
            },
        ),
        migrations.CreateModel(
            name='OriginalNewsSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(help_text='Short (and commonly used) name', max_length=200, unique=True)),
                ('slug', models.SlugField(help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', max_length=200)),
                ('fullname', models.CharField(help_text='If set, the full name will be used in some places instead of the name', blank=True, max_length=200)),
                ('url', models.CharField(max_length=255)),
                ('logo', sorl.thumbnail.fields.ImageField(upload_to='partners', blank=True, null=True)),
                ('article_count', models.IntegerField(editable=False, default=0)),
            ],
            options={
                'verbose_name': 'partner',
            },
        ),
        migrations.CreateModel(
            name='OriginalNewsSourceTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('language_code', models.CharField(verbose_name='Language', db_index=True, max_length=15)),
                ('description', ckeditor.fields.RichTextField(help_text='Text to appear in Parnet page', blank=True, null=True)),
                ('master', models.ForeignKey(to='spacescoops.OriginalNewsSource', null=True, related_name='translations', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'partner translation',
            },
        ),
        migrations.AddField(
            model_name='originalnews',
            name='original_news_source',
            field=models.ForeignKey(to='spacescoops.OriginalNewsSource', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='spacescoops.Category', related_name='articles'),
        ),
        migrations.AddField(
            model_name='article',
            name='original_news',
            field=models.ManyToManyField(to='spacescoops.OriginalNewsSource', related_name='articles', through='spacescoops.OriginalNews'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(verbose_name='Tags', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', to='taggit.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='originalnewssourcetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'slug'), ('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
