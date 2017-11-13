# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Company Name', max_length=120)),
                ('subtitle', models.TextField(default='Subtitle', max_length=1000)),
                ('paragraph', models.TextField(default='Description', max_length=1000)),
                ('input_placeholder', models.CharField(default='Email', max_length=25)),
                ('button_placeholder', models.CharField(default='Submit', max_length=15)),
                ('featured', models.CharField(choices=[('featured', 'Featured'), ('hidden', 'Hidden')], default='hidden', max_length=20)),
            ],
        ),
    ]
