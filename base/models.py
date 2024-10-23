from django.db import models

# Create your models here.


class PersonalDetails(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    career_objective = models.TextField()
    phone_number = models.CharField(max_length=15)  
    email = models.EmailField()  
    picture = models.ImageField(upload_to='profile_pic/') 

    def __str__(self):
        return self.name


class Education(models.Model):
    qualification = models.CharField(max_length=50)
    institution = models.CharField(max_length=100)
    year_of_graduation = models.IntegerField()
    marks = models.FloatField()

    def __str__(self):
        return self.qualification



class Skill(models.Model):
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name



class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)
    project_link = models.URLField(max_length=200)
    thumbnail = models.ImageField(upload_to='project_thumbnails/', null=True, blank=True)


    def __str__(self):
        return self.project_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name