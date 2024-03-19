from django.db import models
from django.contrib.auth.models import User

# Create your models here.

RATING = ((0, "Unsatisfactory"), (1, "Below Average"), (2, "Satisfactory"), (3, "Good"), (4, "Excellent"))

class Comments(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f""