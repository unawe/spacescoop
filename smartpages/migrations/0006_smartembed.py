# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('smartpages', '0005_auto_20160106_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartEmbed',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(unique=True, blank=True, db_index=True, max_length=100, help_text='Internal code to identify tha embed; if set, do not modify. When in doubt, leave empty.')),
                ('creation_date', models.DateTimeField(null=True, auto_now_add=True)),
                ('modification_date', models.DateTimeField(null=True, auto_now=True)),
            ],
            options={
                'verbose_name': 'Embed',
            },
        ),
        migrations.CreateModel(
            name='SmartEmbedTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('language_code', models.CharField(db_index=True, verbose_name='Language', max_length=15)),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='content')),
                ('master', models.ForeignKey(related_name='translations', null=True, to='smartpages.SmartEmbed', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'embed translation',
            },
        ),
        migrations.AlterField(
            model_name='smartpage',
            name='code',
            field=models.CharField(unique=True, blank=True, db_index=True, max_length=100, help_text='Internal code to identify tha page; if set, do not modify. When in doubt, leave empty.'),
        ),
        migrations.AlterUniqueTogether(
            name='smartembedtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
