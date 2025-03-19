from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    home_content = Home.objects.first()
    about_content = About.objects.first()
    skills = Skill.objects.all()
    skilled = Skilled.objects.first()
    works = Work.objects.all()

    if request.method == 'POST':
        name = request.POST.get('flname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')

    return render(request, 'portfolio/index.html', {
        'home_content': home_content,
        'about_content': about_content,
        'skills': skills,
        'skilled': skilled,
        'works': works,
    })
