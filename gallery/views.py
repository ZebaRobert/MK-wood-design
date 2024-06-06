from django.http import HttpResponse
from django.shortcuts import render


def gallery_reviews(request):
    return render(request, "gallery/gallery.html")