from django import forms

from .models import Feedback

class Feedback_Form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
        'rating',
        'feedback'

        ]
