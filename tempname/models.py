from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    avatar = CloudinaryField(
        'avatar',
        default='default/avatarPH',
        folder='avatar/'
    )
    phone_number = models.CharField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'custom_user'