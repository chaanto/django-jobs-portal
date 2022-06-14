from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser) :
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    
    #Rewrite username on AbstractUser
    username = None
    
    #Declare that username changed to email 
    USERNAME_FIELD = 'email'
    
    #Declare required fields here 
    REQUIRED_FIELDS= []