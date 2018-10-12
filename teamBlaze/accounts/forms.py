from django import forms

class infoForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.CharField(label='Email', max_length=50)
