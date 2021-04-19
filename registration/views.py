from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .utils import unique_entry_pass_generator
from django.core.mail import send_mail
from django.forms.models import model_to_dict

from .models import Attendee, Count
from .forms import AttendeeRegistrationForm
# Create your views here.

def home(request):
    count_obj =  Count.objects.get(pk=1)
    form = AttendeeRegistrationForm()
    return render(request,'home/home.html',{'form':form,'count':count_obj})

def registration(request):
    context = {
        'success':False,
        'exists': False,
        'seats':True,
        'number':False,
    }
    if request.method == 'POST' and request.is_ajax():
        form = AttendeeRegistrationForm(request.POST)
        if form.is_valid():
            count_obj =  Count.objects.get(pk=1)
            if count_obj.seats_available():
                count_obj.counter += 1
                count_obj.save()
                email = form.cleaned_data['email']
                if Attendee.objects.filter(email=email).exists():
                    context['exists'] = True
                    return JsonResponse(context,status=500)
                data = form.save(commit=False)
                data.entry_pass = unique_entry_pass_generator(data)
                data.save()
                request.session['registered'] = True
                context['success'] = True
                return JsonResponse(context)
            context['seats'] = False
        context['number'] = True
    return JsonResponse(context,status=500,safe=False)

def view_attendee(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request,'staff/view_attendee.html')
    return render(request,'staff/not_allowed.html')

def search_attendee(request):
    attendee = Attendee.objects.filter(entry_pass=request.GET['entry_pass']).first()
    if attendee:
        json_data = model_to_dict(attendee)
        data = {
            'success': True,
            'person' : json_data,
        }
        return JsonResponse(data)
    return JsonResponse({'success':False},status=500)

def attended(request):
    if request.user.is_authenticated:
        attendee = Attendee.objects.get(pk=request.GET.get('pk'))
        if attendee:
            attendee.attended = True
            attendee.save()
            return JsonResponse({'success':True})
    return JsonResponse({'success':False},status_code=500)

def all_list(request):
    queryset = Attendee.objects.all
    return render(request,'staff/all.html',{'queryset':queryset})

def update_count(request):
    if request.user.is_authenticated:
        count_obj = Count.objects.get(pk=2)
        count_obj.counter = Attendee.objects.filter(attended=True).count()
        count_obj.save()
    return redirect('login')

def team(request):
    return render(request,'home/team.html')