from django.db import models

# Create your models here.


class DeveloperApplication(models.Model):
    GENDER_CHOICES = [
        ('male', 'ذكر'),
        ('female', 'أنثى'),
    ]

    EDUCATION_CHOICES = [
        ('high_school', 'ثانوية عامة'),
        ('bachelor', 'بكالوريوس'),
        ('master', 'ماجستير'),
        ('phd', 'دكتوراه'),
    ]

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    portfolio = models.URLField(blank=True, null=True)
    experience = models.IntegerField()
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    skills = models.TextField()

    def __str__(self):
        return self.full_name