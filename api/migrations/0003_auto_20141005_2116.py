# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20141005_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created', models.DateField(auto_now=True)),
                ('adminID', models.IntegerField()),
                ('userName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('logInTime', models.DateTimeField()),
                ('logOutTime', models.DateTimeField()),
                ('attemptsLimit', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CrimeReports',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created', models.DateField(auto_now=True)),
                ('requestID', models.IntegerField()),
                ('responseTime', models.IntegerField()),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('timeAndDate', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('results', models.CharField(max_length=50)),
                ('comments', models.CharField(max_length=500)),
                ('isLowerCaste', models.BooleanField(default=False)),
                ('isUpperCaste', models.BooleanField(default=False)),
                ('isYoung', models.BooleanField(default=False)),
                ('isOld', models.BooleanField(default=False)),
                ('isMale', models.BooleanField(default=False)),
                ('isFemale', models.BooleanField(default=False)),
                ('isOther_Gender', models.BooleanField(default=False)),
                ('isMurder', models.BooleanField(default=False)),
                ('isKidnapping', models.BooleanField(default=False)),
                ('isRape', models.BooleanField(default=False)),
                ('isRobbery', models.BooleanField(default=False)),
                ('isOther_Crime', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatrolSchedules',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created', models.DateField(auto_now=True)),
                ('sNo', models.IntegerField()),
                ('responseID', models.IntegerField()),
                ('times', models.CharField(max_length=200)),
                ('patrolArea', models.CharField(max_length=200)),
                ('severetyLevel', models.CharField(max_length=50)),
                ('probableCrime', models.CharField(max_length=50)),
                ('victimClass', models.CharField(max_length=50)),
                ('victimGender', models.CharField(max_length=50)),
                ('victimsAge', models.CharField(max_length=50)),
                ('comments', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResponseUnit',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created', models.DateField(auto_now=True)),
                ('userName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('responseID', models.IntegerField()),
                ('attemptsLimit', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResponseUnit_CurrentInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created', models.DateField(auto_now=True)),
                ('requestID', models.IntegerField()),
                ('responseTime', models.IntegerField()),
                ('isRequestAccept', models.BinaryField(default=False)),
                ('requestAcceptOrRejectTime', models.DateTimeField()),
                ('message', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('logInTime', models.DateTimeField()),
                ('emergencyRequestReceivedTime', models.DateTimeField()),
                ('isEmergencyReceived', models.BooleanField(default=False)),
                ('latitude', models.CharField(max_length=80)),
                ('longitude', models.CharField(max_length=80)),
                ('isExtraUnits', models.BooleanField(default=False)),
                ('patrolAccuracy', models.CharField(max_length=50)),
                ('totalExtraUnits', models.IntegerField()),
                ('isExtremeEmergency', models.BooleanField(default=False)),
                ('distance', models.CharField(max_length=50)),
                ('timeElapsed', models.IntegerField()),
                ('responseUnit', models.ForeignKey(to='api.ResponseUnit')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResponseUnit_DataLog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created', models.DateField(auto_now=True)),
                ('logInTime', models.DateTimeField()),
                ('logOutTime', models.DateTimeField()),
                ('requestID', models.IntegerField()),
                ('isRequestAccept', models.BinaryField(default=False)),
                ('requestAcceptOrRejectTime', models.DateTimeField()),
                ('message', models.CharField(max_length=50)),
                ('responseTime', models.IntegerField()),
                ('caseFinishTime', models.DateTimeField()),
                ('emergencyRequestReceivedTime', models.DateTimeField()),
                ('isEmergencyReceived', models.BooleanField(default=False)),
                ('isExtraUnits', models.BooleanField(default=False)),
                ('totalExtraUnits', models.IntegerField()),
                ('isExtremeEmergency', models.BooleanField(default=False)),
                ('extremeEmergencyActivatedTime', models.DateTimeField()),
                ('responseUnit', models.ForeignKey(to='api.ResponseUnit')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResponseUnit_Location',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created', models.DateField(auto_now=True)),
                ('latitude', models.CharField(max_length=80)),
                ('longitude', models.CharField(max_length=80)),
                ('times', models.DateTimeField()),
                ('patrolAccuracy', models.CharField(max_length=50)),
                ('responseUnit', models.ForeignKey(to='api.ResponseUnit')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='crimereports',
            name='responseUnit',
            field=models.ForeignKey(to='api.ResponseUnit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crimereports',
            name='subject',
            field=models.ForeignKey(to='api.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crimereports',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject_location',
            name='times',
            field=models.DateTimeField(),
        ),
    ]
