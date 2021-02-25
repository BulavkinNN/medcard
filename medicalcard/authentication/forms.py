from django.forms import ModelForm
from medcard.models import UserAccount

class Authentication(ModelForm):
    class Meta:
        model = UserAccount
        fields = ['mob_tel','password']