from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('superadmin', 'superadmin'),
<<<<<<< HEAD
        ('Dean', 'Dean'),
=======
        ('mudir', 'mudir'),
>>>>>>> 8ee6f953caf0930deb30e88d38e6ace0e9b42a67
        ('teacher', 'teacher'),
        ('applicant', 'applicant'),
    )

    role = models.CharField(max_length=50, choices=ROLES)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}: {self.role}"
<<<<<<< HEAD

=======
>>>>>>> 8ee6f953caf0930deb30e88d38e6ace0e9b42a67
