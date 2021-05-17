from django.shortcuts import render
from django.http import HttpResponseRedirect
from authentication.permissions import is_doctor
from django.shortcuts import redirect, render
from medcard.models import UserAccount


def my_pacients(request):
    if is_doctor(request):
        user_id = request.user.id

        user = UserAccount.objects.filter(id=user_id)
        return render(request, "pacients/my_pacients.html", {'user': user})
    else:
        return redirect('/')