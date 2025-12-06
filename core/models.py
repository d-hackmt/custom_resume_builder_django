from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields if needed, for now standard User is enough
    # but we use CustomUser to be future proof and match settings
    pass

class Resume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resumes')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    website = models.URLField(max_length=500, blank=True)
    linkedin = models.URLField(max_length=500, blank=True)
    contact = models.CharField(max_length=50)
    briefIntro = models.TextField()
    
    # JSON fields for array data
    expert = models.JSONField(default=list)
    education = models.JSONField(default=list)
    languages = models.JSONField(default=list)
    experience = models.JSONField(default=list)
    skills = models.JSONField(default=list)
    interests = models.JSONField(default=list)
    
    version = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    # Original used 'archieve' (typo), fixing to 'archive' but can alias if needed
    archive = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.user.username} (v{self.version})"
