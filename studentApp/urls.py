from django.urls import path
from .views import *

urlpatterns = [
    path("/applicatn", Applicant),
    path("/document", Document)
]