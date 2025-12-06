import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_builder.settings')
django.setup()

from core.models import CustomUser, Resume

def verify():
    print("Verifying Migration...")
    
    # 1. Create User
    email = "test@example.com"
    if not CustomUser.objects.filter(email=email).exists():
        user = CustomUser.objects.create_user(username=email, email=email, password="password123")
        print(f"User created: {user.email}")
    else:
        user = CustomUser.objects.get(email=email)
        print(f"User exists: {user.email}")
        
    # 2. Create Resume
    resume = Resume.objects.create(
        user=user,
        name="Test User",
        email=email,
        contact="1234567890",
        address="123 Street",
        briefIntro="A test resume",
        expert=["Coding", "Design"],
        education=[{"degree": "BS", "uni": "University", "start": "2020", "end": "2024"}],
        skills=[{"skillName": "Python", "skillPer": "90"}],
        interests=["Coding"]
    )
    print(f"Resume created with ID: {resume.id}, Expert: {resume.expert}")
    
    # 3. Retrieve Resume
    fetched_resume = Resume.objects.filter(user=user).first()
    if fetched_resume:
        print(f"Resume retrieved successfully: {fetched_resume.name}")
        print("Verification PASSED")
    else:
        print("Resume retrieval FAILED")

if __name__ == "__main__":
    verify()
