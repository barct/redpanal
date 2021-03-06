# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 14:25
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images/projects/%Y_%m', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True),
        ),
    ]
