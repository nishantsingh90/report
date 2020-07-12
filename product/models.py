from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime 





MY_CHOICES = (('1', 'environmental incident'),
              ('2', 'injury/illness'),
              ('3', 'property damage'),
              ('4', 'vehicle'))

CHOICES2 = (('1', 'severe'),
              ('2', 'moderate'),
              ('3', 'easy'))
              

CHOICES3 = (('1', 'corporate head office'),
              ('2', 'branch office'))
              
              
class Report(models.Model):
    
    location = models.CharField(max_length=30,choices=CHOICES3)
    incident_description = models.CharField(max_length=100)
    date_and_time_of_incident = models.DateTimeField(default=datetime.now(), blank=True)
    incident_location = models.CharField(max_length=100)
    initial_severity = models.CharField(max_length=30,choices=CHOICES2)
    suspected_cause = models.CharField(max_length=100)
    immediate_actions_taken= models.CharField(max_length=100)
    sub_incident_types =MultiSelectField(choices=MY_CHOICES,max_choices=3,)
    reported_by = models.CharField(max_length=100)
    