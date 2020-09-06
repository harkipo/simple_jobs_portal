from django.contrib.auth.models import User
from .models import *
from django.contrib import auth, messages
import pdb
from recruiter.models import *


def candidate_register_logic(request):
    """

    POST Request -> This function registers a candidate

    """
    obj = request.POST
    print(obj)
    name = obj['name']
    email = obj['email']
    current_ctc = obj['current_ctc']
    expected_ctc = obj['expected_ctc']
    password = obj['password']
    skill_select = obj.getlist('skill_select')
    try:
        user = User.objects.create_user(
            username=email, email=email, first_name=name, password=password)
        candidate = Candidate.objects.create(user=user, current_ctc=int(
            current_ctc), expected_ctc=int(expected_ctc))
        for id in skill_select:
            CandidateSkill.objects.create(
                candidate=candidate, skill_id=int(id))
        messages.success(request, "Registered Successfully please Log-In")
        return True
    except:
        messages.error(request, "Email already registered")
        return False


def login_logic(request, mode):
    """

    POST Request - This is generic login function for both recruiter and candidate

    """
    # pdb.set_trace()
    username = request.POST.get("username")
    password = request.POST.get("login_password")
    request.session['mode'] = mode
    print("username>>>>", username)
    print("password>>>", password)
    user_existed = User.objects.filter(username=username)
    if user_existed:
        user_existed = user_existed[0]
        if mode == 'candidate':
            is_candidate = Candidate.objects.filter(user=user_existed)
            if not is_candidate:
                user_existed = None
        else:
            is_recruiter = Recruiter.objects.filter(user=user_existed)
            if not is_recruiter:
                user_existed = None

    else:
        user_existed = None
    print("user_existed>>>", user_existed)
    if not user_existed:
        messages.success(request, f"{mode} not found")

        return False

    user = auth.authenticate(username=username, password=password)
    print("user>>>", user)
    if not user:
        messages.success(request, "Incorrect Credentials")

        return False
    else:
        username = user_existed.username
        request.session['username'] = username
        # pdb.set_trace()
        auth.login(request, user)
        return True


def applied_jobs_logic(request):
    """

    This function returns applied jobs of candidate

    """
    # pdb.set_trace()
    data = CandidateJob.objects.select_related(
        'job').filter(candidate=request.user.candidate)
    print(data)
    return data


def browse_jobs_logic(request):
    """

    This function returns relevant jobs according to candidate's skills and current CTC

    """
    # pdb.set_trace()
    final_jobs = []
    filtered_jobs = Job.objects.none()                   # to make an empty queryset
    candidate_skills = CandidateSkill.objects.filter(    # Get all skills of a candidate
        candidate=request.user.candidate).values_list('skill_id', flat=True)
    for skill in candidate_skills:                       # Get relevant jobs according to skills
        jobs = JobSkill.objects.select_related('job').filter(skill_id=skill)
        filtered_jobs = filtered_jobs | jobs

    filtered_jobs = filtered_jobs.filter(                # showonly those jobs whose CTC is greater than candidate's current CTC
        job__ctc__gte=request.user.candidate.current_ctc)
    filtered_jobs = filtered_jobs.order_by('job__ctc')

# code to remove duplicates from queryset as .distinct() was not working
    final_job_ids = []
    for job in filtered_jobs:
        if job.job_id not in final_job_ids:
            final_job_ids.append(job.job_id)
            final_jobs.append(job)
    print(">>>>>", final_job_ids)
##
    applied_job_ids = CandidateJob.objects.filter(
        candidate=request.user.candidate).values_list('job_id', flat=True)
    return {"jobs": final_jobs, "applied_job_ids": applied_job_ids}


def apply_job_logic(request):
    """

    This function is called when candidate apply on job 

    POST -> when applying on multiple jobs at once

    GET -> when applying on a single job

    """
    if request.method == 'POST':
        job_ids = request.POST.getlist('job_select')
        for id in job_ids:
            CandidateJob.objects.create(
                job_id=id, candidate=request.user.candidate)
        messages.success(
            request, f"Successfully applied for {len(job_ids)} jobs!")
    else:
        job_id = request.GET.get('job_id')
        CandidateJob.objects.create(
            job_id=job_id, candidate=request.user.candidate)
        messages.success(request, f"Successfully applied for a Job")
    return True
