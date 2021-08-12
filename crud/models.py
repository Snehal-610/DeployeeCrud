from django.db import models
from django.db.models.base import Model

# Create your models here.
class AllData(models.Model):
    AllEmail = models.EmailField(max_length=100,unique=True)
    AllPassword = models.CharField(max_length=100)    

class RegisterData(models.Model):
    alldata = models.ForeignKey(AllData,on_delete=models.CASCADE)
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100,unique=True)
    Password = models.CharField(max_length=100)
    Create = models.DateField(auto_now_add=True)
    ProfilePic = models.ImageField(upload_to="Practice/")