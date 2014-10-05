from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models, connection

class Subject(models.Model):
    id = models.AutoField(primary_key=True,)
    created = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    
    