from django.db import models
from django.contrib.auth.models import User
from candidate.models import Skill , Candidate


class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True,null=True)

    class Meta:
        db_table = 'recruiter'

class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, primary_key=False)
    position = models.CharField(max_length=200,blank=True,null=True)
    company_name = models.CharField(max_length=200,blank=True,null=True)
    ctc = models.IntegerField(blank=True,null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'job'

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, primary_key=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, primary_key=False)

    class Meta:
        db_table = 'job_skill'

class CandidateJob(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, primary_key=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, primary_key=False)
    status = models.CharField(max_length=20,blank=True,null=True,default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'candidate_job'