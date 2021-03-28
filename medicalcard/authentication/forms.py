from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AuthenticationCustomForm(AuthenticationForm):

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
