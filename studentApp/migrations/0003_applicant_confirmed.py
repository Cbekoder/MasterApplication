# Generated by Django 5.0.4 on 2024-04-20 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0002_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
