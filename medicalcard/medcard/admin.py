from django.contrib import admin

# Register your models here.
from .models import Patient,  Doctor, Analysis
from .models import UserAccount


# admin.site.register(UserAccount)

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):

    list_display = ['username','email','get_id_patient','get_id_doctor','is_active']
    fields = ['username','password', 'first_name', 'last_name', 'patronymick',
              'date_of_birth','sex', 'email','mob_tel','city','date_joined',
              'last_login','is_superuser', 'is_staff',  'is_active',
                ]





admin.site.register(Patient)
admin.site.register(Doctor)

admin.site.register(Analysis)
