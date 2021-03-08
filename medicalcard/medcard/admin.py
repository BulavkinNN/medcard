from django.contrib import admin

# Register your models here.
from .models import Patient, MedicalHistory, Doctor, Clinical, MedicalProcedure
from .models import Operation, Examination, Vaccination, MedicalPurpose, Analysis
from .models import UserAccount


# admin.site.register(UserAccount)

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['username','email','get_id_patient','get_id_doctor','is_active']


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Clinical)

admin.site.register(MedicalProcedure)
admin.site.register(MedicalHistory)

admin.site.register(Examination)
admin.site.register(Vaccination)
admin.site.register(Analysis)
admin.site.register(MedicalPurpose)
admin.site.register(Operation)
