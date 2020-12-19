from django.contrib import admin

from .models import Blog, CustomUser


admin.site.register(CustomUser)
admin.site.register(Blog)