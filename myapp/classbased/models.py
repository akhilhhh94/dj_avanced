from django.db import models


class ClassSample(models.Model):
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=500)


class ProxyClassSample(ClassSample):
    class Meta:
        proxy = True
