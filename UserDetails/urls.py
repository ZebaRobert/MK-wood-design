from django.urls import path
from .views import profilePage

urlpatterns = [
    path("", profilePage, name="profile"),
]