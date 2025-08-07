from django.contrib import admin
<<<<<<< HEAD
from mainAPP.models import *

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)
=======
from .models import *


admin.site.register(CoreModel)
admin.site.register(Country)
admin.site.register(Region)
>>>>>>> 8ee6f953caf0930deb30e88d38e6ace0e9b42a67
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Subject)
admin.site.register(SubjectTeacher)