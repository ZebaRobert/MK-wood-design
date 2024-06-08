from django.urls import path
from .views import profilePage, login_view , register_view , logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('profile/', profilePage, name="profile"),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name="logout"),
]