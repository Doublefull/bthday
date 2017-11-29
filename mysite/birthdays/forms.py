from django import forms

class ContactForm(forms.Form):
   subject = forms.CharField()
   email = forms.EmailField(required=False)
   message = forms.CharField()


class BirthdayForm(forms.Form):
    name  = forms.CharField()
    date = forms.DateField(required=False)
    email = forms.EmailField()
   
