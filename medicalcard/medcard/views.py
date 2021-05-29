from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone as tz

from authentication.permissions import is_patient, is_doctor
from django.shortcuts import redirect, render
from .models import UserAccount

from medcard.models import Patient


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
  I am pacient! But there is error
    '''
    context = {}
    if is_patient(request):
        patient_id = request.user.patient.id

        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            print("Error")
        else:
            today = tz.localtime(tz.now()).date()
            context['today'] = today
            context['patient'] = patient

            return render(request, 'medcard/patient_main.html', context=context)

    return HttpResponse(response)


@login_required
def doctor(request):
    user_id = request.user.id

    user_info = UserAccount.objects.filter(id=user_id)
    user = {}
    # TODO: Add clinical id to dict

    return render(request, "medcard/doctor.html", {'user_info': user_info})
