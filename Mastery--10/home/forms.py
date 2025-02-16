from django import forms

class register(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()

class loginuser(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()