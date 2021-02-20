from django.contrib import admin

# Register your models here.
from .models import Patient, MedicalHistory, Doctor, Clinical, MedicalProcedures
from .models import Operation, Examination, Vaccination, MedicalPurpose, Analysis

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Clinical)

admin.site.register(MedicalProcedures)
admin.site.register(MedicalHistory)

admin.site.register(Examination)
admin.site.register(Vaccination)
admin.site.register(Analysis)
admin.site.register(MedicalPurpose)
admin.site.register(Operation)



