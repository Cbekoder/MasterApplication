from django.contrib import admin
from .models import *


admin.site.register(CoreModel)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Subject)
admin.site.register(SubjectTeacher)