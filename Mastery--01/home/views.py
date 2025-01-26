from django.shortcuts import render

#First App Views Function
def homeapp1(request):
    value = {
        'name':'Django',
        'Year':'1'
    }
    return render(request,'home/home.html',value)

def homeapp2(request):
    value = {
        'name':'Django',
        'Year':'2'
    }
    return render(request,'home/home2.html', context=value)

#Second App Views Function
def homeapp3(request):
    value = {
        'name':'Python',
        'Year':'3'
    }
    return render(request,'home2/home2.html', {
        'name':'Python',
        'Year':'4'
    })

def homeapp4(request):
    value = {
        'name':'Python',
        'Year':'4'
    }
    return render(request,'home2/home3.html', value)