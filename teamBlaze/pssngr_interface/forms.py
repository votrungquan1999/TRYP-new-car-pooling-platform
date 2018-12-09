from django import forms

STATE_CHOICE = (("Alabama", "AL"),
                ("Alaska", 'AK'),
                ('Arizona', "AZ"),
                ('Arkansas', 'AR'),
                ('California', 'CA'),
                ('Colorado', 'CO'),
                ('Connecticut', 'CT'),
                ('Delaware', 'DE'),
                ('Florida', 'FL'),
                ('Georgia', 'GA'),
                ('Hawaii', 'HI'),
                ('Idaho', 'ID'),
                ('Illinois', 'IL'),
                ('Indiana', 'IN'),
                ('Iowa', 'IA'),
                ('Kansas', 'KS'),
                ('Kentucky', 'KY'),
                ('Louisiana', 'LA'),
                ('Maine', 'ME'),
                ('Maryland', 'MD'),
                ('Massachusetts', 'MA'),
                ('Michigan', 'MI'),
                ('Minnesota', 'MN'),
                ('Mississippi', 'MS'),
                ('Missouri', 'MO'),
                ('Montana', 'MT'),
                ('Nebraska', 'NE'),
                ('Nevada', 'NV'),
                ('New Hampshire', 'NH'),
                ('New Jersey', 'NJ'),
                ('New Mexico', 'NM'),
                ('New York', 'NY'),
                ('North Carolina', 'NC'),
                ('North Dakota', 'ND'),
                ('Ohio', 'OH'),
                ('Oklahoma', 'OK'),
                ('Oregon', 'OR'),
                ('Pennsylvania', 'PA'),
                ('Rhode Island', 'RI'),
                ('South Carolina', 'SC'),
                ('South Dakota', 'SD'),
                ('Tennessee', 'TN'),
                ('Texas', 'TX'),
                ('Utah', 'UT'),
                ('Vermont', 'VT'),
                ('Virginia', 'VA'),
                ('Washington', 'WA'),
                ('West Virginia', 'WV'),
                ('Wisconsin', 'WI'),
                ('Wyoming', 'WY'),
                ('American Samoa', 'AS'),
                ('District of Columbia', 'DC'),
                ('Federated States of Micronesia', 'FM'),
                ('Guam', 'GU'),
                ('Marshall Islands', 'MH'),
                ('Northern Mariana Islands', 'MP'),
                ('Palau', 'PW'),
                ('Puerto Rico', 'PR'),
                ('Virgin Islands', 'VI'),
)

class createNeedRideForm(forms.Form):
    title = forms.CharField(label="Name of the post")
    seats = forms.IntegerField(label="Number of people need a ride")
    departure_state = forms.CharField(label="State of departure", widget=forms.Select(choices=STATE_CHOICE))
    departure_city = forms.CharField(label="City of departure")
    destination_state = forms.CharField(label="State of destination", widget=forms.Select(choices=STATE_CHOICE))
    destination_city = forms.CharField(label="City of destination")
    price = forms.FloatField(label="Price offer per person")
    bags = forms.IntegerField(label="Number of bags carry")
    date = forms.DateField(widget=forms.SelectDateWidget())
    time = forms.TimeField()

class findDriverForm(forms.Form):
    seats = forms.IntegerField
    departure_state = forms.CharField(label="State of departure", widget=forms.Select(choices=STATE_CHOICE))
    departure_city = forms.CharField(label="City of departure")
    destination_state = forms.CharField(label="State of destination", widget=forms.Select(choices=STATE_CHOICE))
    destination_city = forms.CharField(label="City of destination")
    date = forms.DateField(widget=forms.SelectDateWidget())

class addPassengerForm(forms.Form):
    confirm = forms.CharField(label="Please type CONFIRM here", max_length=10)

