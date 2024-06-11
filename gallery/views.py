from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import GalleryImage, Reviews
from .forms import ReviewForm
import random

def gallery_view(request):
    images = GalleryImage.objects.all()
    reviews = list(Reviews.objects.all())
    random.shuffle(reviews)
    selected_reviews = reviews[:5]  # Take 5 random reviews

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': review_form.errors})

    review_form = ReviewForm() if request.user.is_authenticated else None

    return render(request, 'gallery/gallery.html', {
        'images': images,
        'reviews': selected_reviews,
        'review_form': review_form
    })


def review_list_view(request):
    reviews = list(Reviews.objects.all())
    random.shuffle(reviews)
    selected_reviews = reviews[:5]
    reviews_data = [
        {
            "author": review.author.username,
            "rating": review.get_rating_display(),
            "content": review.content,
            "created_on": review.created_on.strftime('%Y-%m-%d %H:%M:%S'),
        }
    for review in selected_reviews]
    return JsonResponse({"reviews": reviews_data})