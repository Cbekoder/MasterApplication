from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
from userApp.models import User
>>>>>>> 8ee6f953caf0930deb30e88d38e6ace0e9b42a67

class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
<<<<<<< HEAD


class Country(CoreModel):
    name = models.CharField(max_length=100)

class Region(CoreModel):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
=======
class Country(CoreModel):
    name = models.CharField(max_length=35)
>>>>>>> 8ee6f953caf0930deb30e88d38e6ace0e9b42a67

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

class Region(CoreModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name


class Faculty(CoreModel):
    name = models.CharField(max_length=255)
    dean = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.name


class Department(CoreModel):
    name = models.CharField(max_length=255)
    head = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name

<<<<<<< HEAD
=======

>>>>>>> 8ee6f953caf0930deb30e88d38e6ace0e9b42a67
class  Major(CoreModel):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Major'
        verbose_name_plural = 'Majors'

    def __str__(self):
        return self.name

class Subject(CoreModel):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.name


class SubjectTeacher(CoreModel):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
<<<<<<< HEAD
        return f'{self.subject} - {self.teacher}'
=======
        return f'{self.subject} - {self.teacher}'

# class


# class Exam(CoreModel):
#     teacher = models.ForeignKey(SubjectTeacher, on_delete=models.SET_NULL, null=True)
#     applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
#     question_file = models.FileField()
#     user_answer = models.FileField(null=True, blank=True)
#     subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
#     status = models.IntegerField(default=2, choices=(
#         (0, 'Rejected'),
#         (1,'Accepted'),
#         (2,'In progress')
#     ))
#     teacher_response = models.CharField(max_length=255)


class InterviewTeacher(CoreModel):
    ...

>>>>>>> 8ee6f953caf0930deb30e88d38e6ace0e9b42a67
