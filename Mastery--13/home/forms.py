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
    interests = forms.MultipleChoiceField(
        choices=[('coding', 'Coding'), ('music', 'Music'), ('reading', 'Reading')])

    # File and URL Fields
    profile_pic = forms.ImageField()
    resume = forms.FileField()
    website = forms.URLField()

    # Others Specialized Fields
    phone_number = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$', error_messages={'invalid': 'Enter a valid phone number.'})
    password = forms.CharField(widget=forms.PasswordInput)
    slug = forms.SlugField()
    ip_address = forms.GenericIPAddressField()
    ratting = forms.DecimalField()
    massage = forms.CharField()


class demoforms(forms.Form):
    name = forms.CharField(
        label='Your Name',
        max_length=100,
        label_suffix=' : ',
        help_text= 'Enter Your Full Name'
    )
    email = forms.EmailField(
        label ='Email',
        disabled= True
    )
    pincode = forms.IntegerField(
        label='pincode',
        min_value=100000,
        max_value=999999,
        error_messages ={
            'min_value': 'pincode should be 6 digit must be',
            'max_value': 'pincode should be 6 digit only',
            'error_messages': 'Enter Your Valid Pincode'
        }
    )

    age = forms.FloatField(
        label ='age',
        min_value = 0,
    )

    dath_of_birth = forms.DateField(
        label='date of birth',
        required= False,
        help_text = 'Enter Your Real Birth Date'
    )

    appointment_datetime = forms.DateTimeField(
        label = 'datetime',
        required = False
    )

    

