from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'About.html')


def projects(request):
    return render(request, 'Projects.html')


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        # Validation
        if len(name) < 2 or len(email) < 3 or len(message_text) < 4:
            messages.error(request, "Please fill the form correctly.")
            return render(request, 'Contact.html')

        # Save to database
        ins = models.Contact(name=name, email=email, message=message_text)
        ins.save()

        messages.success(request, "Your message has been sent!")
        return render(request, 'Contact.html')

    return render(request, 'Contact.html')
