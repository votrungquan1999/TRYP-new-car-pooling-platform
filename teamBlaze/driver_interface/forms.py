from django import forms

class carForm(forms.Form):
    seats = forms.IntegerField(label="Number of seats")
    year = forms.IntegerField(label="Year that your car is manufactured")
    model = forms.CharField(label="Model of the car", max_length=100)
    manufacturer = forms.CharField(label="Manufacturer of the car", max_length=100)

class createCarPool(forms.Form):
    seats = forms.IntegerField(label="Number of seats available")
