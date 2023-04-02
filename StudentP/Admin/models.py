from django.db import models

class Admin(models.Model):
    Admin_Name = models.CharField(max_length=50)
    Admin_Designation = models.CharField(max_length=50)
    Admin_Password = models.CharField(max_length=50)
    Phone = models.IntegerField()
