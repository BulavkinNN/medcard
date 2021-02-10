from django.http import HttpResponse


def index(request):
    response = '''
    <a href="\\admin">Admin</a>
    <a href="\\registration">Registration</a>
    <a href="\\medcard">Откроется после проверки пароля</a>

    <p>Hello. In this page authentication</p>
    <p> Нужен фон с врачами, и табличка логин, пароль.
        Проверка пароля, в случае не пустого заполнения, </br>и
        отсутствия перебросить на регистрацию.
        Ниже описание:
        Medcard - элетронная медицинская карта пациента,</br>
        позволяет просматривать медицинскую историю и тд тп.
    </p>
    '''
    return HttpResponse(response)
