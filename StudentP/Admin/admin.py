from django.contrib import admin
from Admin.models import Admin

class Amin(admin.ModelAdmin):
    list_display=('Admin_Name','Admin_Designation','Admin_Password','Phone')

admin.site.register(Admin,Amin)
