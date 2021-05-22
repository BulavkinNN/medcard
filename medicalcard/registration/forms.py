from django import forms

from medcard.models import UserAccount


class NewUser(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    job = forms.CharField(label='Job', max_length=30)
    medical_insurance = forms.BooleanField(label='Medical insurance', required=False, initial=False)
    PATIENT = 'patient'
    DOCTOR = 'doctor'
    CHOICES = ((PATIENT, 'I am patient'),
               (DOCTOR, 'I am doctor'))

    user_role = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = UserAccount
        exclude = ("is_staff",
                   "is_active",
                   "date_joined",
                   "last_login",
                   "is_superuser",
                   "groups",
                   "user_permissions")

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError("Password don`t match")
            return cd['password2']
