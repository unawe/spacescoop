# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
        ('spacescoops', '0004_auto_20160120_2138'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='originalnewssourcetranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='originalnewssourcetranslation',
            name='master',
        ),
        migrations.RemoveField(
            model_name='originalnews',
            name='original_news_source',
        ),
        migrations.AddField(
            model_name='originalnews',
            name='institution',
            field=models.ForeignKey(to='institutions.Institution', null=True, on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(related_name='articles', to='spacescoops.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='original_news',
            field=models.ManyToManyField(through='spacescoops.OriginalNews', related_name='scoops', to='institutions.Institution'),
        ),
        migrations.AlterField(
            model_name='article',
            name='spaceawe_category',
            field=models.CharField(help_text='Category for Space Awareness website', choices=[('space', 'Space Exploration'), ('planet', 'Earth Observation'), ('nav', 'Navigation'), ('herit', 'Islamic heritage')], max_length=20, blank=True),
        ),
        migrations.DeleteModel(
            name='OriginalNewsSource',
        ),
        migrations.DeleteModel(
            name='OriginalNewsSourceTranslation',
        ),
    ]
