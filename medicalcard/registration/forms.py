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
    #new_patient = forms.BooleanField(label='I am patient', required=False, initial=False)

    class Meta:
        model = UserAccount
        exclude = ("is_staff",
                   "is_active",
                   "date_joined",
                   "last_login",
                   "is_superuser",
                   "groups",
                   "user_permissions")

        # widgets = {
        #     # telling Django your password field in the mode is a password input on the template
        #     'password': forms.PasswordInput(),
        #     'password2':forms.PasswordInput()
        # }
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError("Password don`t match")
            return cd['password2']

    # name = forms.CharField(max_length=20)
    # surname = forms.CharField(max_length=20)
    # patronymick = forms.CharField(max_length=20)
    # mail = forms.EmailField(max_length=256)
    # sex = forms.CharField(max_length=10)
    # date_of_birth = forms.DateField()
    # password = forms.CharField(max_length=100)
    # city = forms.CharField(max_length=20)
    # job = forms.CharField(max_length=20)
    # medical_insurance = forms.BooleanField()
