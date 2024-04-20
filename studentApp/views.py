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



# # views.py

# from django.http import HttpResponse
# from .forms import ApplicationForm
# from studentApp.models import Application
# from django.core.mail import send_mail

# def apply_for_masters(request):
#     if request.method == 'POST':
#         form = ApplicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             ism = form.cleaned_data.get('ism')
#             familiya = form.cleaned_data.get('familiya')
#             gender = form.cleaned_data.get('gender')
#             country = form.cleaned_data.get('country')
#             region = form.cleaned_data.get('region')
#             address = form.cleaned_data.get('address')
#             tel = form.cleaned_data.get('tel')
#             passport_ser = form.cleaned_data.get('passport_ser')
#             passport_num = form.cleaned_data.get('passport_num')
#             diploma_num = form.cleaned_data.get('diploma_num')
#             certificate_num = form.cleaned_data.get('certificate_num')
#             email = form.cleaned_data.get('email')
#             file = request.FILES['file']
#             application = Application.objects.last()
#             application.file = file
#             application.save()
#             subject = 'Ariza Qabul Qilindi'
#             message = f'Sizning arizangiz muvaffaqiyatli qabul qilindi va saqlandi. Biz tez orada siz bilan bog\'lanamiz.'
#             email_from = 'your_email@example.com'
#             recipient_list = [email, ]
#             send_mail(subject, message, email_from, recipient_list)
            
#             return HttpResponse('Arizangiz muvaffaqiyatli qabul qilindi.')
#     else:
#         form = ApplicationForm()
#     return render(request, 'Applications.html', {'form': form})
