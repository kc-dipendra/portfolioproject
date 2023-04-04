from django.db import models

class Teacher(models.Model):
    Teacher_Name = models.CharField(max_length=50)
    Teacher_Qualification = models.CharField(max_length=50, blank=True)
    Teacher_Subject = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Phone = models.IntegerField()
