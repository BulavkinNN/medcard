from django.shortcuts import render
from django.http import HttpResponseRedirect
from authentication.permissions import is_doctor
from django.shortcuts import redirect, render
from medcard.models import UserAccount, Visit


def my_visits(request):
    # TODO: check if visit already closed
    if not is_doctor(request):
        return redirect('/')

    user_id = request.user.id

    visits_obj = Visit.objects.filter(doctor=user_id).order_by('-date_time')

    return render(request, 'visits/my_visits.html', {'visits': visits_obj})