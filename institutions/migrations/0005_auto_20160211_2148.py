# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def move_locations(apps, schema_editor):
    Institution = apps.get_model('institutions', 'Institution')
    Location = apps.get_model('institutions', 'Location')
    for institution in Institution.objects.all():
        if institution.city or institution.country:
            location = Location.objects.create(city=institution.city, country=institution.country, latitude=institution.latitude, longitude=institution.longitude)
            institution.location = location
            institution.save()


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0004_auto_20160207_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
            ],
            options={
                'ordering': ['country', 'city'],
            },
        ),
        migrations.AddField(
            model_name='person',
            name='spaceawe_node',
            field=models.BooleanField(default=False, verbose_name='Space Awareness node'),
        ),
        migrations.AlterField(
            model_name='person',
            name='citable_name',
            field=models.CharField(help_text='Required for astroEDU activities', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='spaceawe_partner',
            field=models.BooleanField(default=False, verbose_name='Space Awareness partner'),
        ),
        migrations.AddField(
            model_name='institution',
            name='location',
            field=models.ForeignKey(null=True, blank=True, to='institutions.Location', on_delete=models.CASCADE),
        ),

        migrations.RunPython(move_locations),

        migrations.RemoveField(
            model_name='institution',
            name='city',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='country',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='longitude',
        ),

    ]
