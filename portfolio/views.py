from django.shortcuts import render
from .models import *
from .utils import *


def home_page(request):
    main_text = MainText.objects.first()
    project_counter = ProjectCounter.objects.first()
    main_photos = MainPhoto.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    blogs = Blog.objects.all()
    contact = Contact.objects.first()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        send_gmail(email, name, message)

    context = {
        'main_text': main_text,
        'project_counter': project_counter,
        'main_photos': main_photos,
        'skills': skills,
        'projects': projects,
        'blogs': blogs,
        'contact': contact,
    }
    return render(request, 'index.html', context=context)