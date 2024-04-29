from django.http import HttpResponse
from django.views import generic
from .models import About
from django.shortcuts import render

class AboutP(generic.ListView):
    querryset = About.objects
    template_name = "index/index.html"

def index(request):
    return render(request, 'index/index.html')