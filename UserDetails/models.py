from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.

class CustomUser(AbstractUser):
    avatar = CloudinaryField(
        'avatar',
        default='default/avatarPH',
        folder='avatar/'
    )
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'custom_user'