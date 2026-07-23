from django import forms

class Contact(forms.Form):
    contact_email = forms.CharField(label="Email address", max_length=150)
    subject = forms.CharField(label="Subject", max_length=250)
    body = forms.CharField(label="Message", max_length=2000)
