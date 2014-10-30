<<<<<<< HEAD
'''
Created on Oct 10, 2014

@author: ishan
'''
=======
>>>>>>> 680f91b712db3ce989e815f8ecdf12c5541a001a
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models, connection

class Subject(models.Model):
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    userID = models.IntegerField()
    
    

class Subject_Location(models.Model):
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    subject = models.ForeignKey(Subject)
    latitude = models.CharField(max_length=80)
    longitude = models.CharField(max_length=80)
    times = models.DateTimeField()
    

class Subject_DataLog(models.Model):#Information repository entity. Current Info entity not implemented
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    subject = models.ForeignKey(Subject)
    requestID = models.IntegerField()
    emergencyRequestReceivedTime = models.CharField(max_length=50)
    startingEmergencyLatitude = models.CharField(max_length=80)
    startingEmergencyLongitude = models.CharField(max_length=80)
    

class ResponseUnit(models.Model):
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    responseID = models.IntegerField()
    attemptsLimit = models.IntegerField()
    

class ResponseUnit_Location(models.Model):
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    responseUnit = models.ForeignKey(ResponseUnit)
    latitude = models.CharField(max_length=80)
    longitude = models.CharField(max_length=80)
    times = models.DateTimeField()
    patrolAccuracy = models.CharField(max_length=50)
    

class ResponseUnit_DataLog(models.Model):
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    responseUnit = models.ForeignKey(ResponseUnit)
    logInTime = models.DateTimeField()
    logOutTime = models.DateTimeField()
    requestID = models.IntegerField()
    isRequestAccept = models.BinaryField(default=False)
    requestAcceptOrRejectTime = models.DateTimeField()
    message = models.CharField(max_length=50)
    responseTime = models.IntegerField()
    caseFinishTime = models.DateTimeField()
    emergencyRequestReceivedTime = models.DateTimeField()
    isEmergencyReceived = models.BooleanField(default=False)
    isExtraUnits = models.BooleanField(default=False)
    totalExtraUnits = models.IntegerField()
    isExtremeEmergency = models.BooleanField(default=False)
    extremeEmergencyActivatedTime = models.DateTimeField()
    
    
class ResponseUnit_CurrentInfo(models.Model):
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    responseUnit = models.ForeignKey(ResponseUnit)
    requestID = models.IntegerField()
    responseTime = models.IntegerField()
    isRequestAccept = models.BinaryField(default=False)
    requestAcceptOrRejectTime = models.DateTimeField()
    message = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    logInTime = models.DateTimeField()
    emergencyRequestReceivedTime = models.DateTimeField()
    isEmergencyReceived = models.BooleanField(default=False)
    latitude = models.CharField(max_length=80)
    longitude = models.CharField(max_length=80)
    isExtraUnits = models.BooleanField(default=False)
    patrolAccuracy = models.CharField(max_length=50)
    totalExtraUnits = models.IntegerField()
    isExtremeEmergency = models.BooleanField(default=False)
    distance = models.CharField(max_length=50)
    timeElapsed = models.IntegerField()
    
class CrimeReports(models.Model):
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    responseUnit = models.ForeignKey(ResponseUnit)
    subject = models.ForeignKey(Subject)
    requestID = models.IntegerField()
    responseTime = models.IntegerField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    timeAndDate = models.DateTimeField()
    location = models.CharField(max_length=100)
    results = models.CharField(max_length=50)
    comments = models.CharField(max_length=500)
    isLowerCaste = models.BooleanField(default=False)
    isUpperCaste = models.BooleanField(default=False)
    isYoung = models.BooleanField(default=False)
    isOld = models.BooleanField(default=False)
    isMale = models.BooleanField(default=False)
    isFemale = models.BooleanField(default=False)
    isOther_Gender = models.BooleanField(default=False)
    isMurder = models.BooleanField(default=False)
    isKidnapping = models.BooleanField(default=False)
    isRape = models.BooleanField(default=False)
    isRobbery = models.BooleanField(default=False)
    isOther_Crime = models.BooleanField(default=False)
    
class PatrolSchedules(models.Model):
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    sNo = models.IntegerField()
    responseID = models.IntegerField()
    times = models.CharField(max_length=200)
    patrolArea = models.CharField(max_length=200)
    severetyLevel = models.CharField(max_length=50)
    probableCrime = models.CharField(max_length=50)
    victimClass = models.CharField(max_length=50)
    victimGender = models.CharField(max_length=50)
    victimsAge = models.CharField(max_length=50)
    comments = models.CharField(max_length=50)
    
class Administrator(models.Model):
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    adminID = models.IntegerField()
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    logInTime = models.DateTimeField()
    logOutTime = models.DateTimeField()
    attemptsLimit = models.IntegerField()


    
    
    
    
    
    
    
    
    
    
    
   
    
       
    
    
    
    