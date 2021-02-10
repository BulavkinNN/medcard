from django.http import HttpResponse


def index(request):
    response = '''
    I am in index MedCard</br>
    Тут вся информация о этом пациентеб</br>


    <a href="\\statis">Статистика</a>
    '''

    return HttpResponse(response)
