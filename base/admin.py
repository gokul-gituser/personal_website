from django.contrib import admin


from .models import PersonalDetails, Education , Skill, Project

admin.site.register(PersonalDetails)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)