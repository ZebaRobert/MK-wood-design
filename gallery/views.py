from django.shortcuts import render
from .models import GalleryImage, Comments
import random

def gallery_view(request):
    images = GalleryImage.objects.all()
    reviews = list(Comments.objects.all())
    random.shuffle(reviews)
    reviews = reviews[:5]  # Take 5 random reviews
    return render(request, 'gallery/gallery.html', {'images': images, 'reviews': reviews})
