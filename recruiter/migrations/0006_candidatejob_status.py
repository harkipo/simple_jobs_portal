# Generated by Django 3.0.8 on 2020-09-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0005_job_posted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatejob',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=20, null=True),
        ),
    ]