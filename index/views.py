from django.http import HttpResponse
from django.views import generic
from .models import About
from django.shortcuts import render

class AboutListView(generic.ListView):
    queryset = About.objects.all()
    template_name = "index/index.html"
    context_object_name = 'about_list'

def index(request):
    about_list = About.objects.all()
    return render(request, 'index/index.html', {'about_list': about_list})
