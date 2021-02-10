from django.http import HttpResponse


def index(request):
    response='''
    Тут будет статистика по этому пациенту.
    '''
    return HttpResponse(response)