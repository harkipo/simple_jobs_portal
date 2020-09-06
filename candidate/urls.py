from django.urls import path
from . import views
from django.urls import reverse


urlpatterns = [
    
    path('register', views.candidate_register, name='candidate_register'),
    path('login', views.candidate_login, name='candidate_login'),
    path('logout', views.logout_user, name='logout_user'),
    path('jobs/all', views.browse_jobs, name='browse_jobs'),
    path('jobs/aplied', views.applied_jobs, name='applied_jobs'),
    path('jobs/apply', views.apply_job, name='apply_job'),

]