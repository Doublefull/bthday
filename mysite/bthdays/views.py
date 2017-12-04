# Create your views here.

from django.shortcuts import render


#from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from bthdays.forms import  BthdayForm
from django.core.mail import send_mail, get_connection


from bthdays.models import Bthdays

def thanks(request):
    return HttpResponse("Thanks")


@csrf_exempt
def bthdays(request):
    if request.method == 'POST':
        form = BthdayForm(request.POST)
        if form.is_valid():

           f_name =  form.cleaned_data['name']
           f_date = form.cleaned_data['date']
           f_email = form.cleaned_data['email']

           b = Bthdays.objects.create(name=f_name, email=f_email,date=f_date)

           subject =  ('birthday')
           message = ('Today is the birthday of %s' % b.name)
           sender = ('rondatfljak@gmail.com')
           recipients =[b.email] # [form.cleaned_data['email'], email2, email3]

           send_mail(subject, message, sender, recipients)
           return HttpResponseRedirect('/contact/thanks/')
    else:
        form = BthdayForm()
    return render_to_response('contact_form.html', {'form': form})



def bthdays_search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            bth_obj = Bthdays.objects.filter(name__icontains=q) # if field name of enty Bthdays object contains query
            return render_to_response('search_results.html',
                {'bth_obj': bth_obj, 'query': q})
    return render_to_response('search_form.html',
        {'error': error})

