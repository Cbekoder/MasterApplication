from django.db import models
from django.contrib.auth.models import User

class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(CoreModel):
    name = models.CharField(max_length=100)

class Region(CoreModel):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'

    def __str__(self):
        return self.name


class District(CoreModel):
    TYPE = (
        ('city', 'city'),
        ('district', 'district'),
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

    def __str__(self):
        return self.name


class Faculty(CoreModel):
    name = models.CharField(max_length=255)

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
        return f'{self.subject} - {self.teacher}'