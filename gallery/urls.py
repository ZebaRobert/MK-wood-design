from django.urls import path
from .views import gallery_view, review_list_view

urlpatterns = [
    path('', gallery_view, name='gallery'),
    path('reviews/', review_list_view, name='reviews'),
]