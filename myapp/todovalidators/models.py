from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.encoding import smart_text
from django.utils.translation import gettext_lazy as _

from .baseModel import BaseModel
from .validator import validate_even



class TotoQuerySet(models.QuerySet):
    def published(self):
        return self.filter(title__icontains="best")


# Create your models here.
class TodoManager(models.Manager):
    # todo.objects.filter(title__icontains="st").published() will not work, so we declare a query set
    # for querySet , override the default get_queryset()
    def get_queryset(self):
        return TotoQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    '''
    IMPORTANT
    -Get the value like this -
    from django.contrib.auth.models import User
    abc = User.objects.first()
    abc.todo_set.all()

    '''
    # here todo.objects.published() otherwise todo.blbl.published()
    objects = TodoManager()

    def __unicode__(self):  # python 2
        return smart_text(self.title)  # self.title

    def __str__(self):  # python 3
        return smart_text(self.title)

    def save(self, *args, **kargs):
        validate_even(self.title)
        super().save(*args, **kargs)

    def isPublished(self):
        return self.publish_status == self.PublishCoice.PUBLISHED


def pre_save_signal_sample(sender, instance, *args, **kwargs):
    instance.title = instance.title + " test Data"


pre_save.connect(pre_save_signal_sample, sender=todo)
