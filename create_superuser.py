import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_builder.settings')
django.setup()

from core.models import CustomUser

username = "admin"
email = "admin@example.com"
password = "admin"

try:
    if not CustomUser.objects.filter(username=username).exists():
        print(f"Creating superuser '{username}' with email '{email}' and password '{password}'")
        CustomUser.objects.create_superuser(username=username, email=email, password=password)
    else:
        print(f"Superuser '{username}' already exists. Resetting password to '{password}'")
        u = CustomUser.objects.get(username=username)
        u.set_password(password)
        u.is_staff = True
        u.is_superuser = True
        u.save()
    print("Superuser created successfully.")
except Exception as e:
    print(f"Error creating superuser: {e}")
