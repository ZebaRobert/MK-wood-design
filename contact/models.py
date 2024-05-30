from django.db import models

# Create your models here.

# Storing contact submissions

class ContactSubmissions(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject