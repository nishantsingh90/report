from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    MY_CHOICES = (('1', 'environmental incident'),
              ('2', 'injury/illness'),
              ('3', 'property damage'),
              ('4', 'vehicle'))

    CHOICES2 = (('1', 'severe'),
              ('2', 'moderate'),
              ('3', 'easy'))
              

    CHOICES3 = (('1', 'corporate head office'),
              ('2', 'branch office'))
    sub_incident_types= forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=MY_CHOICES)
    initial_severity=forms.ChoiceField(choices=CHOICES2,
                                widget=forms.Select(),
                                required=True)
    location=forms.ChoiceField(choices=CHOICES3,
                                widget=forms.Select(),
                                required=True)
    class Meta:
        model =Report
        fields = '__all__'
      