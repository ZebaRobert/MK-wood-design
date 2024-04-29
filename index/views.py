from django.http import HttpResponse
from django.views import generic
from .models import About


class AboutP(generic.ListView):
    querryset = About.objects
    template_name = "index/index.html"

def index(request):

    return HttpResponse("Hello, world. You're at the index.")