from django.contrib import admin

from .models import ProfileInfo, UserProfile

admin.site.register(UserProfile)
admin.site.register(ProfileInfo)
