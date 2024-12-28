from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    name = models.CharField(max_length=255, blank=True)  # Name can be blank
    email = models.EmailField(max_length=255, blank=True) # Email can be blank or null
    bio = models.TextField(blank=True, null=True)  # Bio can be blank or null
    company = models.CharField(max_length=255, blank=True, null=True)  # Company (optional)
    role = models.CharField(max_length=255, blank=True, null=True)  # Role (optional)
    work_experience = models.TextField(blank=True, null=True)  # Add work_experience field
    education = models.TextField(blank=True, null=True) 
    years_of_experience = models.IntegerField(blank=True, null=True)  # Years of experience (optional)
    project_name = models.CharField(max_length=255)  # Project Name (mandatory)
    project_link = models.URLField(max_length=255, blank=True, null=True)  # Project Link (optional)
    certification_name = models.CharField(max_length=255, blank=True, null=True)  # Certification Name (optional)
    certification_link = models.URLField(max_length=255, blank=True, null=True)  # Certification Link (optional)


    def __str__(self):
        return self.name if self.name else "Unnamed Portfolio"
