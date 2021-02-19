from django.contrib import admin

# Register your models here.
from .models import Patient, Main, Doctor, Clinical, MedicalProcedures

admin.site.register(Patient)
admin.site.register(Main)
admin.site.register(Doctor)
admin.site.register(Clinical)
admin.site.register(MedicalProcedures)