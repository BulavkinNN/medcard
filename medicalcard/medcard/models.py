from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAccount(AbstractUser):
    mob_tel = models.CharField(max_length=20, unique=True)
    patronymick = models.CharField(max_length=20)
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    sex = models.CharField(choices=GENDER_CHOICES, max_length=6)
    date_of_birth = models.DateField(null=True)
    city = models.CharField(max_length=20, null=True)
    USERNAME_FIELD = 'mob_tel'

    def get_id_patient(self):
        item = UserAccount.objects.get(pk=self.pk)
        return str(item.patient.pk)

    def get_id_doctor(self):
        item = UserAccount.objects.get(pk=self.pk)
        return str(item.doctor.pk)


class Clinical(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"Dr. {self.user_account} {self.clinical}"


class MedicalProcedure(models.Model):
    name = models.CharField(max_length=20)
    in_clinik = models.ForeignKey(Clinical, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return f"{self.name} {self.in_clinik}"


class MedicalHistory(models.Model):
    date = models.DateField()
    medical_procedures = models.ForeignKey(MedicalProcedure, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f" {self.date}{self.medical_procedures} "


class Patient(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=20)
    medical_insurance = models.BooleanField()
    my_doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        try:
            first_name = self.user_account.first_name
            last_name = self.user_account.last_name
        except AttributeError:
            return self.id
        else:
            return f"{first_name} {last_name}"


class Record(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.date} {self.patient}"


class ListManipulation(models.Model):
    name = models.CharField(max_length=30)
    component_list = models.JSONField(default=dict)


class Manipulation(models.Model):
    name = models.ForeignKey(ListManipulation, on_delete=models.DO_NOTHING)
    description = models.JSONField(default=dict)
    initiator_doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    executor_clinical = models.ForeignKey(Clinical, on_delete=models.DO_NOTHING, null=True, blank=True)
    record = models.ForeignKey(Record, on_delete=models.DO_NOTHING)


class MedProc(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f" {self.date}{self.patient} "

    class Meta:
        abstract = True


class Examination(MedProc):
    time = models.TimeField(auto_now=True)
    visit_purpose = models.CharField(max_length=256, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    patient_status = models.CharField(max_length=256, null=True)


class Vaccination(MedProc):
    vaccine = models.CharField(max_length=256, null=True)
    info = models.CharField(max_length=256, null=True)


class Analysis(MedProc):
    name_analysis = models.CharField(max_length=256, null=True)
    result_analysis = models.CharField(max_length=256, null=True)


class MedicalPurpose(MedProc):
    direction = models.CharField(max_length=256, null=True)


class Operation(MedProc):
    name = models.CharField(max_length=256, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    info = models.CharField(max_length=256, null=True)
