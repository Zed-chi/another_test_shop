from django.contrib import admin

from .models import Profile, UserProfile

admin.site.register(UserProfile)
admin.site.register(Profile)
