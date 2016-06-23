from __future__ import unicode_literals
from django.db import models
from cuser.models import CUser


class Profile(models.Model):
    TYPES = (
        ('Admin', 1),
        ('Reviewer', 2),
        ('User', 3),
    )
    user = models.OneToOneField(
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


class Reviewer(models.Model):
    user = models.OneToOneField(
        CUser,
        on_delete=models.CASCADE,
    )
    confirmed = models.BooleanField()
    linkedin = models.URLField(null=True)
    position = models.CharField(max_length=50, null=True)
    current_job = models.CharField(max_length=100, null=True)
    previous_job = models.CharField(max_length=100, null=True)
    total_years = models.PositiveIntegerField(null=True)
    bs_subject = models.CharField(max_length=50, null=True)
    bs_university = models.CharField(max_length=50, null=True)
    ms_subject = models.CharField(max_length=50, null=True)
    ms_university = models.CharField(max_length=50, null=True)
    phd_subject = models.CharField(max_length=50, null=True)
    phd_university = models.CharField(max_length=50, null=True)
    summary = models.CharField(max_length=255, null=True)