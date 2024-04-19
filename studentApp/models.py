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
    guruh = models.CharField(max_length=10)
    tuman = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    manzil = models.CharField(max_length=255)
    talim_turi = models.CharField(max_length=255, choices=TALIM_TURI)
    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'

    def __str__(self):
        return f"{self.ism} {self.familiya} {self.otasi}"