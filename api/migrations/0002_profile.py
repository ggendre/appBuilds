# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phoneNumber', models.CharField(max_length=45, blank=True)),
                ('accountEnabled', models.BooleanField(default=True)),
                ('accountCreationSecretKey', models.CharField(max_length=45, blank=True)),
                ('apps', models.ManyToManyField(to='api.App', null=True, blank=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='api.Team', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
            },
            bases=(models.Model,),
        ),
    ]
