from django.db import models
from mainAPP.models import *
from studentApp.models import *

class Examiners(models.Model):
    exam_id = models.ForeignKey('WrittenExam', on_delete=models.CASCADE)
    user_id = models.ForeignKey(SubjectTeacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('exam_id', 'user_id')
        
class WrittenExam(models.Model):
    exam_date = models.DateField()
    exam_time = models.TimeField()
    duration = models.DurationField()
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    question_file = models.FileField(upload_to='Exam_questions/')

    def __str__(self):
        return self.subject
class Exam(CoreModel):
    exam_detail = models.ForeignKey(WrittenExam, on_delete=models.SET_NULL, null=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    user_answer = models.FileField(upload_to='User_answers/')
    status = models.IntegerField(default=2, choices=(
        (0, 'Rejected'),
        (1,'Accepted'),
        (2,'In progress')
    ))
    teacher_response = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'

    def __str__(self):
        return self.exam_detail.subject


class ExamResult(CoreModel):
    examiner = models.ForeignKey(Examiners, on_delete=models.SET_NULL, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    mark = models.SmallIntegerField(default=0)
    description = models.TextField(blank=True, null=True)


class InterviewQuestionnaire(models.Model):
    interview_date = models.DateField()
    interview_time = models.TimeField()
    duration = models.DurationField()
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    question_file = models.FileField(upload_to='Interview_questions/')

    def __str__(self):
        return self.subject

class Interviewer(CoreModel):
    interviewer = models.ForeignKey(SubjectTeacher, on_delete=models.CASCADE)
    interview_id = models.ForeignKey(InterviewQuestionnaire, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.interviewer} | {self.interview_id}"


class InterviewEvaluation(CoreModel):
    interview_id = models.ForeignKey(InterviewQuestionnaire, on_delete=models.SET_NULL, null=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    committee_member = models.ForeignKey(Interviewer, on_delete=models.CASCADE) 
    scores = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField(blank = True)

    def __str__(self):
        return f'{self.applicant.n} | {self.committee_member}'
