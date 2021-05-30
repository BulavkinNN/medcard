from django import forms


class EditDoctor(forms.Form):
    patronymick = forms.CharField(label='Patronymic', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control'}))