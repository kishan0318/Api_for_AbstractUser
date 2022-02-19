from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

# Create your models here.
class User(AbstractUser):
    
    mobile=models.CharField(max_length=11)
    gender=models.CharField(max_length=5,choices=(('1','Male'),('2', 'Female')))
    profile_image=models.ImageField(upload_to='profile_image')
    id_proof=models.FileField(upload_to='id_proof')
    

    def __str__(self):
        return self.email 
