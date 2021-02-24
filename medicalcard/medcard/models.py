from django.db import models



class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymick = models.CharField(max_length=20)
    mail = models.EmailField(max_length=256)
    sex = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=20, null=True)

    class Meta:
        abstract = True


class UserAccount(models.Model):
    mob_tel = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)


class Clinical(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Doctor(User):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"Dr. {self.surname} {self.name}"

class MedicalProcedure(models.Model):
    name = models.CharField(max_length=20)

    in_clinik = models.ForeignKey(Clinical, on_delete = models.DO_NOTHING,default=1)

    def __str__(self):
        return f"{self.name} {self.in_clinik}"

class MedicalHistory(models.Model):
    date = models.DateField()
    medical_procedures = models.ForeignKey(MedicalProcedure, on_delete = models.DO_NOTHING, null=True)

    def __str__(self):
        return f" {self.date}{self.medical_procedures} "


class Patient(User):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=20)
    medical_insurance = models.BooleanField()
    my_doctor = models.ForeignKey(Doctor, on_delete = models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

class MedProc(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete = models.DO_NOTHING, null=True)
    clinical = models.ForeignKey(Clinical, on_delete = models.DO_NOTHING, null=True)

    def __str__(self):
        return f" {self.date}{self.patient} "

    class Meta:
        abstract = True

class Examination(MedProc):
    time=models.TimeField(auto_now=True)
    visit_purpose = models.CharField(max_length=256, null=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.DO_NOTHING, null=True)
    patient_status  = models.CharField(max_length=256, null=True)

class Vaccination(MedProc):
    vaccine = models.CharField(max_length=256,  null=True)
    info = models.CharField(max_length=256,  null=True)

class Analysis(MedProc):
    name_analysis = models.CharField(max_length=256,  null=True)
    result_analysis = models.CharField(max_length=256,  null=True)


class MedicalPurpose(MedProc):
    direction = models.CharField(max_length=256, null=True)

class Operation(MedProc):
    name = models.CharField(max_length=256, null=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.DO_NOTHING, null=True)
    info = models.CharField(max_length=256,  null=True)




