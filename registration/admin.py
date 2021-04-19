from django.contrib import admin
from .models import Attendee,Count
# Register your models here.

def send_mail(modeladmin,request,queryset):
    for object in queryset:
        object.mail()
        object.mail_sent = True
        object.save()
send_mail.short_description = 'Send confirmation email'

class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('name','college','entry_pass','attended','mail_sent')
    actions = [send_mail]
    search_fields = ['name','college']
    list_filter = ['mail_sent','attended']

class CountAdmin(admin.ModelAdmin):
    list_display = ('name','counter')
    
admin.site.register(Attendee,AttendeeAdmin)
admin.site.register(Count,CountAdmin)
