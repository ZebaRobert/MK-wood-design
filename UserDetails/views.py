from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, ReviewForm
from gallery.models import Reviews

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'userdetails/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'userdetails/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profilePage(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    user_reviews = Reviews.objects.filter(author=request.user)
    
    return render(request, 'userdetails/profile.html', {
        'form': form,
        'user_reviews': user_reviews
    })

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Reviews, id=review_id, author=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'userdetails/edit_review.html', {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Reviews, id=review_id, author=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('profile')
    return render(request, 'userdetails/delete_review.html', {'review': review})

@login_required
def delete_profile(request):
    user = request.user
    if request.method == 'POST':
        Reviews.objects.filter(author=user).delete()
        logout(request)
        user.delete()
        return redirect('index')
    return render(request, 'userdetails/delete_profile.html')