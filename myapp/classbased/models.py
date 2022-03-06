from django.db import models
from django.conf import settings


class ClassSample(models.Model):
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=500)


class ProxyClassSample(ClassSample):
    class Meta:
        proxy = True


class UserSample(models.Model):
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
