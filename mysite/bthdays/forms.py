
from django import forms


class BthdayForm(forms.Form):
    name  = forms.CharField()
    date = forms.DateField(required=False)
    email = forms.EmailField()



