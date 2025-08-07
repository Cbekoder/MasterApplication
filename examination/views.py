from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from .models import *
from django.views import View



class Exam(View):
    def get(self,request,pk):
        pass
>>>>>>> 8ee6f953caf0930deb30e88d38e6ace0e9b42a67
