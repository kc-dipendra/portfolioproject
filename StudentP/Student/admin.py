from django.contrib import admin
from Student.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=('Name','Roll','Age','Address','Phone')

admin.site.register(Student,StudentAdmin)
