from django.contrib import admin
from Course.models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display=('Course_Name','Course_Fees','Course_Duration')

admin.site.register(Course,CourseAdmin)
