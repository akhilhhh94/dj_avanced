from django.db import models
from django.utils.encoding import smart_text
from .validator import validate_even

# Create your models here.

class todo(models.Model):
    id              = models.BigAutoField(primary_key=True)
    title           = models.CharField(
                            max_length=240)

    def __unicode__(self): #python 2
        return smart_text(self.title) #self.title

    def __str__(self): #python 3
        return smart_text(self.title)

    def save(self, *args, **kargs):
        validate_even(self.title)
        super().save(*args, **kargs)


