from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


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


class Doctor(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True)
    description = models.JSONField(default=dict)

    def __str__(self):
        return f"Dr. {self.user_account}"


class Patient(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=20)
    medical_insurance = models.BooleanField()

    def __str__(self):
        try:
            first_name = self.user_account.first_name
            last_name = self.user_account.last_name
        except AttributeError:
            return str(self.id)
        else:
            return f"{first_name} {last_name}"


class Visit(models.Model):
    date_time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    result = models.JSONField(default=dict)


class Analysis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    date = models.DateField(default=timezone.now)
    result = models.JSONField(default=dict)

    def __str__(self):
        return f"( {self.patient} : {self.date} )"

class Diagnosis(models.Model):
    name = models.CharField(max_length=50)
    description = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class Disease(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.DO_NOTHING, null=True)
    description = models.JSONField(default=dict)

    def __str__(self):
        return f"( {self.patient} : {self.diagnosis} )"