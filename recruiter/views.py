from django.shortcuts import render, HttpResponse, redirect, Http404
from candidate.models import Skill
from . import business_logic as logic
import pdb
from django.contrib.auth import logout
from candidate.business_logic import login_logic
from .models import *


def recruiter_register(request):
    """

    POST Request - This API helps recruiter to register into our system

    """
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            logic.recruiter_register_logic(request)
            return redirect("index")
        else:
            return render(request, 'recruiter/login_signup.html')


def recruiter_login(request):
    """

    POST Request - This API helps user to login into their account. Username and password are passed in the request

    """
    # pdb.set_trace()
    if request.user.is_authenticated or request.method == 'GET':
        return redirect('index')

    else:
        if request.method == 'POST':
            data = login_logic(request, "recruiter")

            return redirect('index')
        else:
            raise Http404()


def post_job(request):
    """

    POST -> This api helps recruiter to post a job

    GET -> Load job post template

    """
    if request.method == "POST":
        response = logic.post_job_logic(request)
        return redirect('view_jobs')

    else:
        skills = Skill.objects.all()
        print(skills)
        return render(request, 'recruiter/post_job.html', {"skills": skills})


def view_jobs(request):
    """

    GET -> To show all the posted jobs of a recruiter

    """
    if request.method == "GET":
        jobs = Job.objects.filter(recruiter=request.user.recruiter)
        return render(request, 'recruiter/view_jobs.html', {"jobs": jobs})
    else:
        raise Http404()


def view_applicants(request, job_id=None):
    """

    GET -> To show all the applicants of a certain job

    """
    if request.method == "GET":
        applicants = CandidateJob.objects.select_related(
            'candidate').filter(job_id=job_id)
        return render(request, 'recruiter/view_applicant.html', {"applicants": applicants})
    else:
        raise Http404()


def approve_candidate(request, job_id=None, candidate_id=None):
    """
    This api approves the application of candidate

    """
    logic.approve_candidate_logic(request, job_id, candidate_id)
    return redirect('view_applicants', job_id=job_id)


def reject_candidate(request, job_id=None, candidate_id=None):
    """
    This api rejects the application of candidate

    """
    logic.reject_candidate_logic(request, job_id, candidate_id)
    return redirect('view_applicants', job_id=job_id)
