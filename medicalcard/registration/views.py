from django.http import HttpResponse


def index(request):
    response='''
    Поля с регистрационными данными пациента</br>
    <ul>
    <li>ФИО</li>
    <li>телефон</li>
    <li>почта (primary key)</li>
    <li>пол</li>
    <li>дата рождения</li>
    <li>город</li>
    <li>место работы</li>
    <li>медстаховка (bool)</li>
    <li>пароль</li>
    <li>повтор пароль</li>
    </ul>
    Далее отправка на email письма с паролем и логином (если успеем)
    и возрат на главную страницу
    '''
    return HttpResponse(response)
