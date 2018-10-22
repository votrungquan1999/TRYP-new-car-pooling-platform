from django import forms
from .models import MyUser

class infoForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'first_name',
            'last_name',
            'email'

        ]

    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.EmailField(label='Email')

    #def clean_email(self, *args, **kwargs):
