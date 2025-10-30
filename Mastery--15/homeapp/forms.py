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