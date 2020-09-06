from django.contrib import admin
from django.urls import path,include
from candidate.views import index , populate_skills

urlpatterns = [
    path('', index, name='index'),
    path('populate/skills', populate_skills, name='populate_skills'),
    path('candidate/',include('candidate.urls')),
    path('recruiter/', include('recruiter.urls')),
   
]
