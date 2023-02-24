# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournaments', '0001_initial'),
        ('divisions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DebateTeamMotionPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.IntegerField(db_index=True, verbose_name='preferences')),
            ],
            options={
                'verbose_name': 'debate team motion preference',
                'verbose_name_plural': 'debate team motion preferences',
            },
        ),
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField(help_text='The order in which motions are displayed', verbose_name='sequence number')),
                ('text', models.TextField(help_text='The full motion e.g., "This House would straighten all bananas"', max_length=500, verbose_name='text')),
                ('reference', models.CharField(help_text='Shortcode for the motion, e.g., "Bananas"', max_length=100, verbose_name='reference')),
                ('info_slide', models.TextField(blank=True, default='', help_text='The information slide for this topic; if it has one', verbose_name='info slide')),
                ('flagged', models.BooleanField(default=False, help_text='For WADL: Allows for particular motions to be flagged as contentious', verbose_name='flagged')),
                ('divisions', models.ManyToManyField(blank=True, to='divisions.Division', verbose_name='divisions')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Round', verbose_name='round')),
            ],
            options={
                'verbose_name_plural': 'motions',
                'verbose_name': 'motion',
                'ordering': ('seq',),
            },
        ),
    ]
