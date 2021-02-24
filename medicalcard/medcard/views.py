from django.http import HttpResponse


def index(request):
    response = '''
    I am in index MedCard</br>
    Тут вся информация о этом пациентеб</br>


    <a href="\\statis">Статистика</a>
    '''

    return HttpResponse(response)

def pocient(request):
    response = '''
  I am pacient!
    '''

    return HttpResponse(response)


def doctor(request):
    response = '''
  I am doctor!
    '''

    return HttpResponse(response)


