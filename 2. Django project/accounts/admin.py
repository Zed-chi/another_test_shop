from django.contrib import admin

from .models import ProfileInfo, UserProfile


admin.site.register(ProfileInfo)


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "id"]
