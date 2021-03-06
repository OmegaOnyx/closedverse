# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-01 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0006_auto_20170731_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yeah',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('type', models.PositiveSmallIntegerField(default=0)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.Comment')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.Post')),
            ],
        ),
    ]
