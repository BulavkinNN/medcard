from django import forms
from medcard.models import Patient
from django.utils import timezone


class AddVisit(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), label='Select patient', widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput(attrs={'class': 'form-control'}))