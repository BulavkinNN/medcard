from django import forms
from medcard.models import Patient
from django.utils import timezone


class AddVisit(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), label='Select patient', widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput(attrs={'class': 'form-control'}))


class EditVisit(forms.Form):
    to_doctors = forms.CharField(label='Medical referral', widget=forms.Textarea(attrs={'class': 'form-control'}))
    to_analysis = forms.CharField(label='Referral for tests', widget=forms.Textarea(attrs={'class': 'form-control'}))
    meds = forms.CharField(label='Drug prescription', widget=forms.Textarea(attrs={'class': 'form-control'}))