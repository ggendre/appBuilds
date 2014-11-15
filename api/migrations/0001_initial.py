# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('technicalName', models.CharField(max_length=90, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bundleName', models.CharField(max_length=90, null=True, blank=True)),
                ('versionNumber', models.CharField(max_length=10)),
                ('creationDate', models.DateTimeField()),
                ('app', models.ForeignKey(to='api.App')),
            ],
            options={
                'ordering': ['app__name', '-versionNumber'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Os',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True, blank=True)),
                ('technicalName', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='build',
            name='os',
            field=models.ForeignKey(to='api.Os'),
            preserve_default=True,
        ),
    ]
