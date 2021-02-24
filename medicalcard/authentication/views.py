from django.shortcuts import render
from .models import Role

def index(request):
    list_role= Role.objects.all()

    context = '''
    <p>
    Выбор роли пациент,врач и возможность добавление</br>
    других профилей в админ панели.</p>
    '''

    return render(request,
                    'authentication/index.html',
                    {"context":context,
                     "list_role":list_role,
                    })



