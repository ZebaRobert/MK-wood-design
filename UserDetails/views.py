from django.http import HttpResponse


def profilePage(request):
    return HttpResponse("Hello, world. You're at the Profile.")