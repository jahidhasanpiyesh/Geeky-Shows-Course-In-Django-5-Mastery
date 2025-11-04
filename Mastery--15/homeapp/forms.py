from django import forms

class userlogin(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


    # Custom Validation for Name Field
    def clean_name(self):
        # name = self.cleaned_data.get('name') # same work this line
        name = self.cleaned_data['name'] # Must be used [] for cleaned data
        if len(name) < 5:
            raise forms.ValidationError("Name must be at Least 5 Characters")
        return name
    
    # Custom Validation for Email Field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('.com'):
            raise forms.ValidationError("Email Must be end With .com")
        elif not "@" in email:
            raise forms.ValidationError("Email Must Contain @ Symbol")
        elif len(email) < 12:
            raise forms.ValidationError("Email Must be Less Than 12 Characters")
        return email