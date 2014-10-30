# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_DataLog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created', models.DateField(auto_now=True)),
                ('requestID', models.IntegerField()),
                ('emergencyRequestReceivedTime', models.CharField(max_length=50)),
                ('startingEmergencyLatitude', models.CharField(max_length=80)),
                ('startingEmergencyLongitude', models.CharField(max_length=80)),
                ('subject', models.ForeignKey(to='api.Subject')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject_Location',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created', models.DateField(auto_now=True)),
                ('latitude', models.CharField(max_length=80)),
                ('longitude', models.CharField(max_length=80)),
                ('times', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(to='api.Subject')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='address',
            new_name='userName',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='name',
        ),
        migrations.AddField(
            model_name='subject',
            name='password',
            field=models.CharField(default=datetime.date(2014, 10, 5), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='userID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
