from django.db import models
from django.conf import settings

# Create your models here.

RATING = ((0, "Unsatisfactory"), (1, "Below Average"), (2, "Satisfactory"), (3, "Good"), (4, "Excellent"))

class Reviews(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="review"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.username} - {self.rating}'

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title