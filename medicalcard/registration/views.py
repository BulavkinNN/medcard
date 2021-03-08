from django.shortcuts import render
from django.http import HttpResponseRedirect

from medcard.models import Patient
from .forms import NewPacient


def index(request):
    return render(request, "registration/index.html")


def create(request):
    if request.method == "POST":
        form = NewPacient(request.POST)
        if form.is_valid():
            patient = Patient()
            patient.name = request.POST.get("name")
            patient.surname = request.POST.get("surname")
            patient.date_of_birth = request.POST.get("date_of_birth")
            patient.medical_insurance = request.POST.get("medical_insurance")
            patient.save()
        return HttpResponseRedirect("/")

    else:
        form = NewPacient()

    return render(request, 'registration/createPacient.html', {'form': form})
