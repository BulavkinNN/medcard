from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from authentication.permissions import is_doctor
from django.shortcuts import redirect, render, get_object_or_404
from medcard.models import UserAccount, Visit, Patient, Doctor
from .forms import AddVisit


def my_visits(request):
    # TODO: check if visit already closed
    if not is_doctor(request):
        return redirect('/')

    user_id = request.user.id

    visits_obj = Visit.objects.filter(doctor=user_id).order_by('-date_time')

    return render(request, 'visits/my_visits.html', {'visits': visits_obj})


def add_visit(request):
    if not is_doctor(request):
        return redirect('/')

    error = True
    if request.method == 'POST':
        form = AddVisit(request.POST)
        if form.is_valid():
            # TODO: Check if date not older than NOW
            visit = Visit(date_time=request.POST.get('date'), doctor=Doctor.objects.get(user_account=request.user.id), patient=Patient.objects.get(pk=request.POST.get('patient')))
            visit.save()

            return redirect('/visits/visit/' + str(visit.id))

    else:
        form = AddVisit()

    return render(request, 'visits/add_visit.html', {'form': form, 'error': error})


def get_visit(request, pk):
    visit = get_object_or_404(Visit, pk=pk)

    return render(request, 'visits/single.html', {'visit': visit})