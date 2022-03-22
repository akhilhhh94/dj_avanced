from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username


def my_user_profile_signal(sender, instance, created, *agrs, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
    else:
        pass


post_save.connect(my_user_profile_signal, sender=settings.AUTH_USER_MODEL)
