from django.contrib import messages
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

    if 'logout_message' in request.session:
        messages.success(request, request.session.pop('logout_message'))

    return render(request, 'index/index.html', {'about_list': about_list, 'current_path': request.path})
