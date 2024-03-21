from django.http import HttpResponse


def gallery(request):
    return HttpResponse("Hello, world. You're at the Gallery.")