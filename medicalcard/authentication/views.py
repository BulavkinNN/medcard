from django.shortcuts import render
from .models import Role
from django.http import HttpResponseRedirect
from .forms import Authentication
from medcard.models import UserAccount


def index(request):

    list_role = Role.objects.all()
    if request.method == "POST":
        context = '''
                       <p>
                      Я уже получил POST запросы</p>
                       '''
        form = Authentication(request.POST)
        if form.is_valid():
            context = '''
                                   <p>
                                  Форма валидна</p>
                                   '''
            mob_tel = form.cleaned_data['mob_tel']
            password = form.cleaned_data['password']
            #role = form.cleaned_data['role'] !!!!!!!!!!!! Запрос
            role = 'pacient'
            if role == 'pacient':
                return HttpResponseRedirect("../medcard/patient")
            if role == 'doctor':
                return HttpResponseRedirect("../medcard/doctor")
    else:
        form = Authentication()
        context = '''
                   <p>
                   Выбор роли пациент,врач и возможность добавление</br>
                   других профилей в админ панели.</p>
                   '''



    return render(request,'authentication/index.html',
                    {"context":context,
                     "list_role":list_role,
                     'form': form
                    })

