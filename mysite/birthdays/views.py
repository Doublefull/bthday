
from django.shortcuts import render


#from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from birthdays.forms import ContactForm, BirthdayForm   
from django.core.mail import send_mail, get_connection


from birthdays.models import Birthdays


@csrf_exempt
def contact(request):    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = ('rondatfljak@gmail.com')
            recipients = [form.cleaned_data['email']] # [form.cleaned_data['email'], email2, email3]
          
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})


def thanks(request):
    return HttpResponse("Thanks")

@csrf_exempt
def birthday(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():

           f_name =  form.cleaned_data['name']
           f_date = form.cleaned_data['date']
           f_email = form.cleaned_data['email']

           b = Birthdays.objects.create(name=f_name, email=f_email,date=f_date)

           subject =  ('birthday')
           message = ('Today is the birthday of %s' % b.name)
           sender = ('rondatfljak@gmail.com')
           recipients =[b.email] # [form.cleaned_data['email'], email2, email3]

           send_mail(subject, message, sender, recipients)
           return HttpResponseRedirect('/contact/thanks/')
    else:
        form = BirthdayForm()
    return render_to_response('contact_form.html', {'form': form})

