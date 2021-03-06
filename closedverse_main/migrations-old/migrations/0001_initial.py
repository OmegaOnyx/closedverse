# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-30 21:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('nickname', models.CharField(blank=True, max_length=32, null=True)),
                ('password', models.CharField(max_length=128)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('avatar', models.CharField(blank=True, max_length=1200)),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('addr', models.GenericIPAddressField(null=True)),
                ('origin_id', models.CharField(blank=True, max_length=16, null=True)),
                ('origin_info', models.CharField(blank=True, max_length=255, null=True)),
                ('staff', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feeling', models.PositiveSmallIntegerField(default=0)),
                ('body', models.TextField(null=True)),
                ('drawing', models.CharField(max_length=200, null=True)),
                ('spoils', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('edited', models.DateTimeField(default=None, null=True)),
                ('status', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('ico', models.URLField(blank=True)),
                ('banner', models.URLField(blank=True)),
                ('platform', models.PositiveSmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityClink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('kind', models.BooleanField(default=False)),
                ('also', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='closedverse_main.Community')),
                ('root', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='closedverse_main.Community')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feeling', models.PositiveSmallIntegerField(default=0)),
                ('body', models.TextField(null=True)),
                ('drawing', models.CharField(max_length=200, null=True)),
                ('url', models.URLField(blank=True, default='', max_length=1200)),
                ('spoils', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('edited', models.DateTimeField(default=None, null=True)),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.Community')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.Community'),
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='original_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closedverse_main.Post'),
        ),
    ]
