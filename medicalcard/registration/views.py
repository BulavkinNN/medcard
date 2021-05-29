from django.shortcuts import render
from django.http import HttpResponseRedirect
from medcard.models import Patient, Doctor
from .forms import NewUser
from django.contrib import messages

def index(request):
    return render(request, "registration/index.html")


def create(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)  # Do not save to table yet
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            if form.cleaned_data['user_role'] == 'patient':
                job = form.cleaned_data['job']
                medical_insurance = form.cleaned_data['medical_insurance']
                new_patient = Patient.objects.create(user_account=new_user,job=job, medical_insurance=medical_insurance)
            elif form.cleaned_data['user_role'] == 'doctor':
                new_doctor = Doctor.objects.create(user_account=new_user)
            messages.success(request, "Add new user!")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "form not valid!")
        return render(request, 'registration/createPatient.html', {'form': form})

    else:
        form = NewUser()

    return render(request, 'registration/createPatient.html', {'form': form})
