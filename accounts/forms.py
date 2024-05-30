# forms.py
from django import forms

class SearchForm(forms.Form):
    destination = forms.CharField(max_length=100, required=False)
    checkin = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    checkout = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    guests = forms.IntegerField(required=False, min_value=1)
