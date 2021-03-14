from django.forms import ModelForm
from medcard.models import UserAccount
from .models import Role


class AuthenticationForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = ['mob_tel', 'password']


class RoleForm(ModelForm):
    """
    Don`t use
    """

    class Meta:
        model = Role
        fields = ['role']
