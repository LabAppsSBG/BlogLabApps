# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-16 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160716_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='imgportada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]