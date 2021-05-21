from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from authentication.permissions import is_patient, is_doctor
from django.shortcuts import redirect, render
from .models import UserAccount


def index(request, message=None):
    context = {'message': message}
    return render(request, template_name="medcard/index.html", context=context)


@login_required
def medcard(request):
    if is_patient(request):
        return redirect('medcard:patient')

    if is_doctor(request):
        return redirect('medcard:doctor')

    raise ValueError("You not doctor or patient, you Harry Houdini")


@login_required
def patient(request):
    response = '''
  I am pacient!
    '''
    return HttpResponse(response)


@login_required
def doctor(request):
    user_id = request.user.id

    user_info = UserAccount.objects.filter(id=user_id)
    user = {}
    # TODO: Add clinical id to dict

    return render(request, "medcard/doctor.html", {'user_info': user_info})
