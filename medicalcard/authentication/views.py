from django.shortcuts import render
from .models import Role
from django.http import HttpResponseRedirect
from .forms import AuthenticationForm
from medcard.models import UserAccount
from django.urls import reverse

def index(request):

    list_role = Role.objects.all()
    if request.method == "POST":
        context = '''
                       <p>
                      Я уже получил POST запросы</p>
                       '''
        form = AuthenticationForm(request.POST)

        if form.is_valid():
            context = '''
                                   <p>
                                  Форма валидна</p>
                                   '''
            mob_tel = form.cleaned_data['mob_tel']
            password = form.cleaned_data['password']
            role = request.POST['role']
            # []with role need get from Role model, not manual!!
            if role in ['pacient','doctor']:
                return HttpResponseRedirect(reverse(role))
    else:
        form = AuthenticationForm()
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

