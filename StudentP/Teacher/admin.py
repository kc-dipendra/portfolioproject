from django.contrib import admin
from Teacher.models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display=('Teacher_Name','Teacher_Qualification','Teacher_Subject','Address','Phone')

admin.site.register(Teacher,TeacherAdmin)
