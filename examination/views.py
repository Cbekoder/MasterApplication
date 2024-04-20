from django.shortcuts import render
from .models import *
from django.views import View



class Exam(View):
    def get(self,request,pk):
        pass