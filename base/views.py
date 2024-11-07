from django.shortcuts import render, get_object_or_404, redirect
from .models import PersonalDetails,Education, Skill, Project
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse  
from urllib.parse import urlencode 
import os

skills = ["Python", "Django", "Pytorch", "scikit-learn",'Numpy','Pandas', "SQL",'PostgreSQL','MySQL',"Data Structures and Algorithms","Matplotlib","Power BI","Git","Data Analysis","Data Mining","Mathematics and Statistics","Artificial Intelligence","Machine Learning","Deep Learning","Computer Vision","Natural Language Processing", 'Agile', 'Jira', ]

   # projects = Project.objects.all()
projects = [
        {
            'id': 1,
            'title': 'Flight Price Prediction',
            'description': 'This project focuses on predicting flight ticket prices using historical flight data. By leveraging various categorical and continuous variables, I developed a regression model to estimate prices accurately.The project enhanced my proficiency in Python and scikit-learn, allowing me to deepen my understanding of data preprocessing techniques.This experience reinforced my ability to translate complex datasets into actionable insights, further solidifying my foundation in data science and machine learning.This project sharpened my problem-solving skills and I learned how to visualize data effectively with Matplotlib.Overall, this project has been instrumental in enhancing my technical expertise and preparing me for future challenges in the field of data science.',
            'link': 'https://colab.research.google.com/drive/1gB0VDBL0r4eI5CSF82gRGuiVa8_uz8Pq?usp=sharing',
            'technologies': 'Python, Scikit-learn, Matplotlib'
        },
        {
            'id': 2,
            'title': 'Computer Vision Model for Food Image Classification',
            'description': 'With a focus on building a robust food classification model, this project applied computer vision and deep learning techniques to accurately identify and categorize diverse food items. By leveraging convolutional neural networks (CNNs) and transfer learning, I developed a model that significantly optimized performance and accuracy. Creating a custom dataset for this specific task also strengthened my skills in data handling and preprocessing with Python. Additionally, using PyTorch allowed me to refine the model and deepen my expertise in neural network implementation. This experience reinforced my foundation in both computer vision and machine learning.',
            'link': 'https://colab.research.google.com/drive/1N3EspASNsQaPkyFlkCKBlrqXzhiaHkGY?usp=sharing',
            'technologies': 'Python, Pytorch, Matplotlib'
        },
        {
            'id': 3,
            'title': 'Chatbot',
            'description': 'This chatbot, developed using Python,FastAPI and Google’s Dialogflow, utilizes advanced natural language processing capabilities to assist users in finding and purchasing products from a virtual store. The integration of Dialogflow enables the chatbot to understand and respond to user queries effectively, handling product inquiries and providing recommendations. Additionally, it helps users add items to their carts, displays the cart contents, and guides them through a simulated purchase process, enhancing the overall shopping experience with seamless interaction and support.',
            'link': 'https://github.com/gokul-gituser/sales-chatbot.git',
            'technologies': 'Python, FastAPI, Google’s Dialogflow, MySQL'
        },
        
        {
            'id': 4,
            'title': 'Personal Portfolio Website',
            'description': 'This Django portfolio website showcases my skills and projects. Built with Django, it features a user-friendly interface that highlights my expertise in Python, Django, PyTorch, and machine learning. Each project includes a detailed description of the technologies used and challenges faced, providing insight into my practical experience.The site has a clean, responsive design, making it easy for visitors to navigate and access information about my work and achievements. Overall, this portfolio reflects my technical capabilities and passion for continuous learning in software development and data science.',
            'link': 'https://github.com/gokul-gituser/personal_website.git',
            'technologies': 'Python, Django, PostgreSQL, HTML, CSS, Bootstrap'
        },
        {
            'id': 5,
            'title': 'Power BI Project',
            'description': 'Developed an interactive Power BI dashboard to analyze key metrics and trends for the 2024 Olympics dataset.Used Power Query for data import and transformation and DAX for custom measures to analyze athlete statistics and medal distribution. Leveraged a variety of visuals to present trends in participation and performance across countries and sports and applied slicers to enable dynamic exploration.This project demonstrated expertise in Power BI’s analytical and visualization tools for actionable data insights.',
            'link': 'https://drive.google.com/drive/folders/1R-6QGLk2wsymws2oOPiARCFrpuWdPsHO?usp=sharing',
            'technologies': 'Power BI, DAX, Power Query'
        },
        
    ]

# Create your views here.
def index(request):
    personal_details = PersonalDetails.objects.first()
    education_details = Education.objects.all()
  #  skills = Skill.objects.all()
    


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


'''
def project_detail(request, project_id):
    
    try:
        project = Project.objects.get(id=project_id) 
    except Project.DoesNotExist:
        raise Http404("Project not found")  
    
    context = {
        'project': project,

        
    }
    return render(request, 'base/project_detail.html', context) 
'''
def project_detail(request, project_id):
    
    project = next((proj for proj in projects if proj['id'] == project_id), None)
    
    if project is None:
        raise Http404("Project not found")  
    
    context = {
        'project': project,
    }
    
    return render(request, 'base/project_detail.html', context)


def contact_view(request):
    show_thank_you_modal = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            show_thank_you_modal = True
    else:
        form = ContactForm()

    return render(request, 'base/index.html', {
        'form': form,
        'show_thank_you_modal': show_thank_you_modal,
    })



