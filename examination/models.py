from django.db import models
from mainAPP.models import *
from studentApp.models import *

class Examiners(models.Model):
    pass

class WrittenExam(models.Model):
    exam_date = models.DateField()
    exam_time = models.TimeField()
    duration = models.DurationField()
    teachers = models.ForeignKey(Examiners, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    question_file = models.FileField()

    def __str__(self):
        return self.subject
class Exam(CoreModel):
    
    applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    user_answer = models.FileField()
    status = models.IntegerField(default=2, choices=(
        (0, 'Rejected'),
        (1,'Accepted'),
        (2,'In progress')
    ))
    teacher_response = models.CharField(max_length=255)

    def __str__(self):
        return self.applicant




