def is_user(request, user_role):
    return hasattr(request.user, user_role)


def is_doctor(request):
    return is_user(request, 'doctor')


def is_patient(request):
    return is_user(request, 'patient')
