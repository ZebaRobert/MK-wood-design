from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                subject,
                f"Message from {name} ({email}):\n\n{message}",
                email,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact/success.html')
