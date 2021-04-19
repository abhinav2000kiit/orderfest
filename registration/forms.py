from django.forms import ModelForm
from .models import Attendee

class AttendeeRegistrationForm(ModelForm):
    
    class Meta:
        model = Attendee
        fields = ['name','email','mobile_number','whatsapp_number','college']

