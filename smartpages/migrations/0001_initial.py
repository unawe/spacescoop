# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmartPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('registration_required', models.BooleanField(verbose_name='registration required', default=False, help_text='If this is checked, only logged-in users will be able to view the page.')),
                ('creation_date', models.DateTimeField(null=True, auto_now_add=True)),
                ('modification_date', models.DateTimeField(null=True, auto_now=True)),
            ],
            options={
                'ordering': ('translations__url',),
                'verbose_name': 'page',
            },
        ),
        migrations.CreateModel(
            name='SmartPageTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language_code', models.CharField(db_index=True, verbose_name='Language', max_length=15)),
                ('url', models.CharField(db_index=True, verbose_name='URL', max_length=100)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content', blank=True)),
                ('master', models.ForeignKey(null=True, to='smartpages.SmartPage', related_name='translations', on_delete=models.CASCADE)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='smartpagetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
