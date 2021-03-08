from django.http import HttpResponse


def index(request):
    response = '''



    I am in index MedCard</br>
    Тут вся информация о этом пациентеб</br>


    <a href="patient\\">Пациент</a>
    <a href="doctor\\">Врач</a>
   
    '''

    return HttpResponse(response)

def patient(request):
    response = '''
  I am pacient!
    '''

    return HttpResponse(response)


def doctor(request):
    response = '''
  I am doctor!
    '''

    return HttpResponse(response)


