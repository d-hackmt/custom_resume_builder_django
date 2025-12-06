from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Resume

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Use default UserAdmin configuration
    pass

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user', 'version', 'active', 'archive')
    list_filter = ('active', 'archive', 'version')
    search_fields = ('name', 'email', 'user__username')
