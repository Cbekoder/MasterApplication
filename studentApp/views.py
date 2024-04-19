from django.shortcuts import render, redirect
from django.views import View
from .models import *


class UploadDocument(View):
    def get(self, request):
        return render(request, "uploadDocument.html")


    def post(self, request):
        if request.user.is_authenticated:
            Student.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            state=request.POST.get("state"),
            zip=request.POST.get("zip"),
            country=request.POST.get("country"),
            )
            return redirect('index')

        return render(request, "uploadFile.html")


class Test(View):
    def get(self, request):
        pass
    def post(self, request):
        pass
