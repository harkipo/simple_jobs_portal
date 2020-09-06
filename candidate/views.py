from django.shortcuts import render , HttpResponse , redirect ,Http404
from .models import Skill
from . import business_logic as logic
import pdb
from django.contrib.auth import logout
from recruiter.models import Job , CandidateJob

def index(request):
    if request.user.is_authenticated:
        if request.session['mode'] == 'candidate':
            return render(request,'candidate/candidate_welcome.html')
        else:
            return render(request,'recruiter/welcome_page.html')

    else:
        skills = Skill.objects.all()
        return render(request,'candidate/login_signup.html',{"skills":skills})


def candidate_register(request):
    """

    POST -> This API helps candidate to register into our system

    GET -> This method loads register template

    """
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            logic.candidate_register_logic(request)
            return redirect("index")
        else:
            skills = Skill.objects.all()
            return render(request,'candidate/login_signup.html',{"skills":skills})


def candidate_login(request):
    """

    POST Request - This API helps user to login into their account. Username and password are passed in the request

    """
    # pdb.set_trace()
    if request.user.is_authenticated or request.method == 'GET':
        return redirect('index')

    else:
        if request.method == 'POST':
            data = logic.login_logic(request,"candidate")

            return redirect('index')
        else:
            raise Http404()


def logout_user(request):
    """
    Created by: Harshit Rastogi  Date: 6 September 2020

    GET Request - This API logouts a user

    """
    # pdb.set_trace()
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')



def browse_jobs(request):
    """

    POST Request - This API shows relevant jobs to the candidate

    """
    context = logic.browse_jobs_logic(request)
    
    return render(request,'candidate/browse_jobs.html',context)


def applied_jobs(request):
    """

    This API shows candidate's applied jobs

    """
    jobs = logic.applied_jobs_logic(request)
    return render(request,'candidate/applied_jobs.html',{"jobs":jobs})


def apply_job(request):
    """

    This API helps candidate to apply on a job

    """
    logic.apply_job_logic(request)
    return redirect('browse_jobs')




def populate_skills(request):
    """

    This api populates dummy data in skills table

    """
    skills = ['ruby on rails',"kafka","aws","python","django","mysql","mongodb","php","laravel","flask","html","javascript","jquery","css","dotnet","c++","c#"]
    for skill in skills:
        Skill.objects.create(name=skill)

    return HttpResponse("Skills added")



