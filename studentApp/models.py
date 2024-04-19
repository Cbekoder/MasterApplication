from django.db import models
from mainAPP.models import *

class Student(CoreModel):
    JINS = (
        ('erkak', 'erkak'),
        ('ayol', 'ayol')
    )

    TALIM_TURI = (
        ('kunduzgi', 'kunduzgi'),
        ('sirtqi', 'sirtqi'),
    )

    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    otasi = models.CharField(max_length=255, blank=True, null=True)
    jins = models.CharField(max_length=10, choices=JINS)
    telefon_shaxsiy = models.CharField(max_length=13)
    telefon_qoshimcha = models.CharField(max_length=13, blank=True, null=True)
    region = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)
    education_type = models.CharField(max_length=255, choices=TALIM_TURI)
    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'

    def __str__(self):
        return f"{self.ism} {self.familiya} {self.otasi}"