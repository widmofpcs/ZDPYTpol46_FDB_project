from django.contrib import admin
from .models import CustomUser, CustomUserProfile

admin.site.register(CustomUser)
admin.site.register(CustomUserProfile)
