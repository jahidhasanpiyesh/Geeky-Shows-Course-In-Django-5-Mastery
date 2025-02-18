from django import forms

class register(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()

class addressinfo(forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    ziicode = forms.IntegerField()

class login(forms.Form):
    email = forms.EmailField()
    # password fields in hidden input section.
    password = forms.CharField(widget=forms.HiddenInput())  
