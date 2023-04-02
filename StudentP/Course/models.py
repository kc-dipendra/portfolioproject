from django.db import models

class Course(models.Model):
    Course_Name = models.CharField(max_length=50)
    Course_Fees = models.IntegerField()
    Course_Duration = models.IntegerField()
