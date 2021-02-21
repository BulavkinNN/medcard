from django import forms

class NewPacient(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    patronymick = forms.CharField(max_length=20)
    mail = forms.EmailField(max_length=256)
    sex = forms.CharField(max_length=10)
    date_of_birth = forms.DateField()
    password = forms.CharField(max_length=100)
    city = forms.CharField(max_length=20)
    job = forms.CharField(max_length=20)
    medical_insurance = forms.BooleanField()