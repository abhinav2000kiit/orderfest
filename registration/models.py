from django.db import models
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.template.loader import get_template
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags



# Create your models here.

class Attendee(models.Model):
    entry_pass = models.CharField(max_length=5,unique=True,null=False,editable=False)
    name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=10,validators=[RegexValidator(r'^[6-9]{1}[0-9]{9}$')])
    whatsapp_number = models.CharField(max_length=10,validators=[RegexValidator(r'^[6-9]{1}[0-9]{9}$')],null=True)
    college = models.CharField(max_length=60,null=True)
    email = models.EmailField()
    attended = models.BooleanField(default=False)
    mail_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def mail(self):
        subject = 'Registration confirmation for The Order Fest '
        html_message = render_to_string('templated_email/confirmation.html', {'name': str(self.name),'pass':str(self.entry_pass)})
        plain_message = strip_tags(html_message)
        send_mail(subject,plain_message,'contact@thewriteorder.com',[str(self.email)],html_message=html_message)

class Count(models.Model):
    name = models.CharField(max_length=15)
    c_id = models.IntegerField(primary_key=True)
    counter = models.PositiveIntegerField(null=True,blank=True)

    def seats_available(self):
        if self.counter < 2000:
            return True
        else:
            return False
    def __str__(self):
        return str(self.name)
    



