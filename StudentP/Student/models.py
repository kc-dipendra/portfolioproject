from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=50)
    Roll = models.IntegerField()
    Age = models.IntegerField()
    Address = models.CharField(max_length=50, blank=True)
    Phone = models.IntegerField()
