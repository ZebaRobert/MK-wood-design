from django.urls import path
from .views import profilePage, login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path("", profilePage, name="profile"),
]