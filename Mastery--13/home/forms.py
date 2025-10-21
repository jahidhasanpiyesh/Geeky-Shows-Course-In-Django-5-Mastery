from django import forms

class homeforms(forms.Form):

    # Basic Fields
    name = forms.CharField()
    email = forms.EmailField()
    pin_code = forms.IntegerField()

    # Additional Fields
    age = forms.FloatField()
    date_of_birth = forms.DateField()
    appointment_time = forms.TimeField()
    appointment_datetime = forms.DateTimeField()
    is_subscribed = forms.BooleanField()
    aggree_terms = forms.NullBooleanField()

    # Choice Fields Two Type Format used to any one

    # gender = forms.ChoiceField(choices=[
    #     ('M', 'Male'), 
    #     ('F', 'Female'), 
    #     ('O', 'Other')
    #     ])
    
    GENDER = [
        ('M', 'Male'), 
        ('F', 'Female'), 
        ('O', 'Other')
        ]
    gender = forms.ChoiceField(choices=GENDER)
    interests = forms.MultipleChoiceField(choices=[('coding', 'Coding'), ('music', 'Music'), ('reading', 'Reading')])
    
    # File and URL Fields
    profile_pic = forms.ImageField()
    resume = forms.FileField()
    website = forms.URLField()

    # Others Specialized Fields
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages={'invalid': 'Enter a valid phone number.'})
    password = forms.CharField(widget=forms.PasswordInput)
    slug = forms.SlugField()
    ip_address = forms.GenericIPAddressField()
    ratting = forms.DecimalField()
    massage = forms.CharField()
