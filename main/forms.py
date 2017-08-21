from main.models import *
from django import forms
from main.form_choices import COUNTY_CHOICES
from django.core.validators import validate_email

class mainForm(forms.ModelForm):

    class Meta:
        model = searchCourtdate
        fields = [ 'first_name', 'last_name', 'county', 'case_number', 'email']
        widgets = {
                'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
                'email': forms.TextInput(attrs={'placeholder': 'Email'}),
                'case_number': forms.TextInput(attrs={'placeholder': 'ex: YY-MM-12345'}),
                # 'county': forms.ChoiceField()
        }
    def __init__(self, *args, **kwargs):
        super(mainForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['case_number'].required = False
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False

class emailForm(forms.ModelForm):

    class Meta:
        model = searchCourtdate
        fields = ['case_number', 'email']
        widgets = {

                'email': forms.TextInput(attrs={'placeholder': 'Email'}),
                'case_number': forms.TextInput(attrs={'placeholder': 'ex: YY-MM-12345'}),
            
        }
