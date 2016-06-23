from __future__ import unicode_literals
from django.db import models
from django import forms
from cuser.models import CUser


class Profile(models.Model):
    TYPES = (
        ('Admin', 1),
        ('Reviewer', 2),
        ('User', 3),
    )
    user = models.ForeignKey(
        CUser,
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(upload_to='photos/', null=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True)
    is_male = models.BooleanField()
    street = models.CharField(max_length=255)
    unit = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    type = models.IntegerField(choices=TYPES, null=True)
