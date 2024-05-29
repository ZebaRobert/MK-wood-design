from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    backgorund_image = CloudinaryField(
        'bgIMG',
        default='default/bgPH',
        folder='background/'
    )
    content = models.TextField()
    
    def __str__(self):
        return self.title