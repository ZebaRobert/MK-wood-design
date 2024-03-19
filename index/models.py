from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_lenght=200, unique=True)
    backgorund_image = CloudinaryField(
        'image',
        default='bg_placeholder'
    )
    content = models.TextField()

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title}"
    
    