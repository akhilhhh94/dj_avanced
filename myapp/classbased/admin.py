from django.contrib import admin

# Register your models here.

from .models import ClassSample, UserSample

admin.site.register(ClassSample)
admin.site.register(UserSample)