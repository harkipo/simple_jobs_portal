# Generated by Django 3.0.8 on 2020-09-06 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_candidate_candidateskill'),
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('ctc', models.IntegerField(blank=True, null=True)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.Recruiter')),
            ],
            options={
                'db_table': 'job',
            },
        ),
        migrations.CreateModel(
            name='JobSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.Job')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.Skill')),
            ],
            options={
                'db_table': 'job_skill',
            },
        ),
    ]
