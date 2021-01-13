from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    TYPE_CHOICES = ( 
    ("user", "USER"), 
    ("nursery", "NURSERY"), 
) 
    user_type = models.CharField(max_length = 20,choices = TYPE_CHOICES,default="user")
    name = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.username
