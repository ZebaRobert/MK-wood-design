from django import forms
from .models import CustomUser
from gallery.models import Reviews
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'avatar']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['content', 'rating']