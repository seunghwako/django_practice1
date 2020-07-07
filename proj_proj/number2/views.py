from django.shortcuts import render


# Create your views here.
def home(request) :
    return render(request, '1.html')

def member1(request) :
    return render(request, 'ksh.html')

def member2(request) :
    return render(request, 'csh.html')
