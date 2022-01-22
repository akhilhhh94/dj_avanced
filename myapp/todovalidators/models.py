from django.db import models
from django.utils.encoding import smart_text
from django.utils.translation import gettext_lazy as _
from .validator import validate_even
from .baseModel import BaseModel


# Create your models here.

class todo(BaseModel):
    class PublishCoice(models.TextChoices):
        PUBLISHED = 'PL', _('Published')
        DRAFT = 'DR', _('Draft')
    title = models.CharField(
                            max_length=240)
    publish_status = models.CharField(
        max_length=2,
        choices=PublishCoice.choices,
        default=PublishCoice.PUBLISHED,
    )

    def __unicode__(self): #python 2
        return smart_text(self.title) #self.title

    def __str__(self): #python 3
        return smart_text(self.title)

    def save(self, *args, **kargs):
        validate_even(self.title)
        super().save(*args, **kargs)

    def isPublished(self):
        return self.publish_status == self.PublishCoice.PUBLISHED


