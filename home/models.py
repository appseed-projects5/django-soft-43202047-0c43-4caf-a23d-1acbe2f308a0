# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Pol(models.Model):

    #__Pol_FIELDS__
    serial = models.CharField(max_length=255, null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)

    #__Pol_FIELDS__END

    class Meta:
        verbose_name        = _("Pol")
        verbose_name_plural = _("Pol")


class Lubs(models.Model):

    #__Lubs_FIELDS__
    serial = models.CharField(max_length=255, null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)

    #__Lubs_FIELDS__END

    class Meta:
        verbose_name        = _("Lubs")
        verbose_name_plural = _("Lubs")



#__MODELS__END
