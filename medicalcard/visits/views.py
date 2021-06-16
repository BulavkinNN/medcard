from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from authentication.permissions import is_doctor
from django.shortcuts import redirect, render, get_object_or_404
from medcard.models import UserAccount, Visit, Patient, Doctor
from .forms import AddVisit, EditVisit


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

            return redirect('/visits/visit/edit/' + str(visit.id))

    form = AddVisit()

    return render(request, 'visits/add_visit.html', {'form': form, 'error': error})


def edit_visit(request, pk):
    if not is_doctor(request):
        return redirect('/')

    updated = False
    visit = Visit.objects.get(pk=pk)
    form = EditVisit()

    if request.method == 'POST':
        form = EditVisit(request.POST)
        if form.is_valid():
            result = dict()

            result['to_doctors'] = request.POST.get('to_doctors')
            result['to_analysis'] = request.POST.get('to_analysis')
            result['meds'] = request.POST.get('meds')

            print(request.POST.get('to_doctors'))

            visit.result = result
            visit.save()

            updated = True

    if visit.result:
        form = EditVisit(
            initial={'to_doctors': visit.result['to_doctors'], 'to_analysis': visit.result['to_analysis'],
                     'meds': visit.result['meds']})

    return render(request, 'visits/edit.html', {'form': form, 'updated': updated, 'visit_id': pk})




def get_visit(request, pk):
    visit = get_object_or_404(Visit, pk=pk)

    return render(request, 'visits/single.html', {'visit': visit})