from django.shortcuts import render
from django.http import HttpResponseRedirect
from authentication.permissions import is_doctor
from django.shortcuts import redirect, render
from medcard.models import Patient, UserAccount


def my_pacients(request):
    if is_doctor(request):
        user_id = request.user.id

        patients_obj = Patient.objects.filter(my_doctor_id=user_id)
        patients = {}

        for patient in patients_obj:
            patient_info = {}
            for user in UserAccount.objects.filter(id=patient.user_account_id):
                patient_info['first_name'] = user.first_name
                patient_info['last_name'] = user.last_name
                patient_info['email'] = user.email
                patient_info['mob_tel'] = user.mob_tel
                patient_info['date_of_birth'] = user.date_of_birth
                patient_info['city'] = user.city
                patient_info['sex'] = user.sex

            patients[patient.user_account_id] = patient_info

        print(patients)
        return render(request, "pacients/my_pacients.html", {'patients': patients})
    else:
        return redirect('/')