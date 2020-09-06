from django.urls import path
from . import views
from django.urls import reverse


urlpatterns = [
    
    path('register', views.recruiter_register, name='recruiter_register'),
    path('login', views.recruiter_login, name='recruiter_login'),
    path('job/post', views.post_job, name='post_job'),
    path('job/view', views.view_jobs, name='view_jobs'),
    path('job/<job_id>/applicants', views.view_applicants, name='view_applicants'),
    path('job/<job_id>/applicant/<candidate_id>/approve', views.approve_candidate, name='approve_candidate'),
    path('job/<job_id>/applicant/<candidate_id>/reject', views.reject_candidate, name='reject_candidate'),

]