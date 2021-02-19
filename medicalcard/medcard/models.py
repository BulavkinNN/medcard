from django.db import models

class Clinical(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymick = models.CharField(max_length=20)
    mail = models.EmailField(max_length=256)
    sex = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Doctor(User):
    #city = models.CharField(max_length=20, default="No city")
    clinical = models.ForeignKey(Clinical, on_delete = models.DO_NOTHING,default=1)
    #models.DO_NOTHING not logic, but SET_NULL, except error
    def __str__(self):
        return f"Dr. {self.surname} {self.name}"

class Patient(User):
    #city = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    medical_insurance = models.BooleanField()
    my_doctor = models.ForeignKey(Doctor, on_delete = models.DO_NOTHING,default=1)
    def __str__(self):
        return f"{self.surname} {self.name}"


class Main(models.Model):
    date = models.DateField()
    #patient = models.ForeignKey(Patient, on_delete = models.DO_NOTHING)


    def __str__(self):
        return f"{self.id} {self.date} {self.patient.__str__()}"

class MedicalProcedures(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
