from django.shortcuts import render
from home.forms import register, loginuser
# Create your views here.

def registation(req):
    # res = register()

    # Fields is position change 
    res = register(field_order=['first_name','email'])
    return render(req, 'home/index.html',{'registation':res})

def login(req):
    # log = loginuser(auto_id='id_%s')  # use to >>>  auto_id='id_%s' id = same field name
    # log = loginuser(auto_id=False)  # use to >>>  auto_id=False  just field name show
    # log = loginuser(auto_id=True)  # use to >>>  auto_id=True  id= field name
    # log = loginuser(auto_id='jahid')   # Just field name show
    # log = loginuser(auto_id='jahid_%s')  # Jahid and field name show
    
    # log = loginuser(label_suffix=' A')  # field ar sathe kiso word add kora jai
    # log = loginuser(label_suffix='')  # field is simple

    # show hidden of info in my web fields  
    log = loginuser(initial={'email':'jahid@gmail.com', 'password':'1234'})  # field is simple
    
    return render(req, 'home/login.html',{'login':log}) 