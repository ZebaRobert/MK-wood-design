from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.

class CustomUser(AbstractUser):
    
    username = models.CharField(max_lenght=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    avatar = CloudinaryField( 
        'avatar',
        default='avatarPH'
    )
    password = models.CharField(max_length=128)


    def __str__(self):
        return self.username