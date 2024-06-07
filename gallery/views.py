from django.shortcuts import render
from django.http import JsonResponse
from .models import GalleryImage, Reviews
import random

def gallery_view(request):
    images = GalleryImage.objects.all()
    reviews = list(Reviews.objects.all())
    random.shuffle(reviews)
    initial_reviews = reviews[:5]  # Take 5 random reviews
    return render(request, 'gallery/gallery.html', {'images': images, 'initial_reviews': initial_reviews})


def review_list_view(request):
    reviews = list(Reviews.objects.all())
    random.shuffle(reviews)
    selected_reviews = reviews[:5]  # Take 5 random reviews
    reviews_data = [
        {
            "author": review.author.username,
            "rating": review.get_rating_display(),
            "content": review.content,
            "created_on": review.created_on.strftime('%Y-%m-%d %H:%M:%S'),
        }
    for review in selected_reviews]
    return JsonResponse({"reviews": reviews_data})