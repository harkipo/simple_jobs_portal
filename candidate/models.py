from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)

    class Meta:
        db_table = 'skill'



class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_ctc = models.IntegerField()
    expected_ctc = models.IntegerField()

    class Meta:
        db_table = 'candidate'



class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, primary_key=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, primary_key=False)

    class Meta:
        db_table = 'candidate_skill'








