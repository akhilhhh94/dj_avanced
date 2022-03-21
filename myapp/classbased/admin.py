from django.contrib import admin

# Register your models here.

from .models import ClassSample, UserSample, AnotherSample

admin.site.register(ClassSample)
admin.site.register(UserSample)
admin.site.register(AnotherSample)