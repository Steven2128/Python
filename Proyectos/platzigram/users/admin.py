from django.contrib import admin
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ("pk", "user", "phone_number", "website", "picture")
    list_disply_links = ("pk", "user")
    list_editable = ("phone_number", "website", "picture")