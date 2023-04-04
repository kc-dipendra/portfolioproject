from django.contrib import admin
from Student.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=('Name','Roll','Age','Address','Phone')
    ordering=('Name',)
#    search_fields = ('name')
#    ordering=('-Name',) -If you want to display by descending order

admin.site.register(Student,StudentAdmin)
