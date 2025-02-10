from django.shortcuts import render
from school.models import All_Student
# Create your views here.
def all_stu(req):
    Data =  All_Student.objects.all()
    return render(req, 'school/alldata.html',{'alldata':Data})


def single_stu(req):
    # single_data = All_Student.objects.get(pk=1)  #using to pk=1 pk mins prymari key
    # single_data = All_Student.objects.get(id=1)  #using to id=1 same
    single_data = All_Student.objects.get(name='Nadim')  # fixing data query data show
    return render(req, 'school/single.html', {'single':single_data})