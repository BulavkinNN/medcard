import hashlib

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponseRedirect

from medcard.models import Patient
from .forms import NewPatient, UserAccount


def index(request):
    return render(request, "registration/index.html")


def create(request):
    if request.method == "POST":
        form = NewPatient(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)  # Do not save to table yet
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            if form.cleaned_data['new_patient']:
                job = form.cleaned_data['job']
                medical_insurance = form.cleaned_data['medical_insurance']
                new_patient = Patient.objects.create(user_account=new_user,job=job, medical_insurance=medical_insurance)
        return HttpResponseRedirect("/")

    else:
        form = NewPatient()

    return render(request, 'registration/createPacient.html', {'form': form})
