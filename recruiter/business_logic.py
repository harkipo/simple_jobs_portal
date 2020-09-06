from django.contrib.auth.models import User
from .models import *
from django.contrib import auth, messages
import pdb


def recruiter_register_logic(request):
    """

    This function saves new recruiter into the system

    """
    obj = request.POST
    print(obj)
    name = obj['name']
    email = obj['email']
    address = obj['address']
    password = obj['password']
    try:
        user = User.objects.create_user(
            username=email, email=email, first_name=name, password=password)
        candidate = Recruiter.objects.create(user=user, address=address)
        messages.success(request, "Registered Successfully please Log-In")
        return True
    except:
        messages.error(request, "Email already registered")
        return False


def post_job_logic(request):
    """
    This function save jobs posted by recruiter

    """
    obj = request.POST
    print(obj)
    position = obj['position']
    company_name = obj['company_name']
    ctc = obj['ctc']
    skills = obj.getlist('skill_select')
    recruiter = Recruiter.objects.filter(user=request.user)
    if recruiter:
        job = Job.objects.create(
            recruiter=recruiter[0], position=position, company_name=company_name, ctc=ctc)
        for skill in skills:
            JobSkill.objects.create(job=job, skill_id=int(skill))
        return True
    else:
        return False


def approve_candidate_logic(request, job_id, candidate_id):
    """
    This api approves the application of candidate

    """
    CandidateJob.objects.filter(
        job_id=job_id, candidate_id=candidate_id).update(status='approved')


def reject_candidate_logic(request, job_id, candidate_id):
    """
    This api rejects the application of candidate

    """
    CandidateJob.objects.filter(
        job_id=job_id, candidate_id=candidate_id).update(status='rejected')
