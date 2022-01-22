from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    sample = models.CharField(
        default=None,
        null=True,
        max_length=240)
    class Meta:
        abstract = True
