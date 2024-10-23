from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
 
path('', views.index, name='index'),
path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
path('download-resume/', views.download_resume, name='download_resume'),

]