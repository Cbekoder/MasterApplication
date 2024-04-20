from django.shortcuts import render, redirect
from django.views import View
from .models import *


class ApplicatResgister(View):
    def get(self, request):
        return render(request, "uploadDocument.html")


    def post(self, request):
        if request.user.is_authenticated:
            Applicant.objects.create(
            user=request.user,
            gender=request.POST.get("gender"),
            tell=request.POST.get("tell"),
            region=request.POST.get("region"),
            country=request.POST.get("country"),
            adress=request.POST.get("adress"),
            pasport_ser=request.POST.get("pasport_ser"),
            passport_num=request.POST.get(""),
            diploma_num=request.POST.get("gender"),
            certificate_num=request.POST.get("gender"),
            )
            return redirect(request,'index.html')

        return render(request, "uploadFile.html")

class Document(View):
    def get(self,request):
        return render(request,"uploadFile.html")
    def post(self,request):
        if request.user.is_authenticated:
            Document.objects.create(
                user=request.user,
                name=request.POST.get("name"),
                file=request.POST.get("file")
            )
            return redirect(request, "index.html")
        return render(request, "uploadFile.html")
