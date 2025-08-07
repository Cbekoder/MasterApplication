from django.db import models
from userApp.models import User
from mainAPP.models import *
from mainAPP.models import CoreModel



class Applicant(CoreModel):
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER)
    tell = models.CharField(max_length=13)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)
    passport_ser = models.CharField(max_length=3)
    passport_num = models.IntegerField()
    diploma_num = models.CharField(max_length=15)
    certificate_num = models.CharField(max_length=35, blank=True, null=True)
    confirmed=models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class Document(CoreModel):
    user = models.ForeignKey('Applicant', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField()