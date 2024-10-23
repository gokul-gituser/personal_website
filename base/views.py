from django.shortcuts import render, get_object_or_404, redirect
from .models import PersonalDetails,Education, Skill, Project
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse  
from urllib.parse import urlencode 
import os

# Create your views here.
def index(request):
    personal_details = PersonalDetails.objects.first()
    education_details = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    form = ContactForm()
    submitted =  request.GET.get('submitted', False)
    

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            query_string = urlencode({'submitted': True})
            return redirect(f"{reverse('base:index')}?{query_string}")
       

    context = {
        'personal_details': personal_details,
        'education_details': education_details,
        'skills': skills,
        'projects': projects,
        'form': form,
        'submitted': submitted,
        
    }

    return render(request, 'base/index.html', context)



def project_detail(request, project_id):
    
    try:
        project = Project.objects.get(id=project_id) 
    except Project.DoesNotExist:
        raise Http404("Project not found")  
    
    context = {
        'project': project,

        
    }
    return render(request, 'base/project_detail.html', context) 


def download_resume(request):
    
    file_path = os.path.join(settings.MEDIA_ROOT, 'resume', 'Gokul-Jayan-J-B-resume.pdf')
    
   
    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Gokul-Jayan-J-B-resume.pdf"'
            return response
    else:
        return HttpResponse("File not found.")


def contact_view(request):
    show_thank_you_modal = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Set the flag to show the thank you modal after submission
            show_thank_you_modal = True
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'show_thank_you_modal': show_thank_you_modal,
    })