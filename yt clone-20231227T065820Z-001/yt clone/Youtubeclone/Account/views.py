from django.shortcuts import render
from django.http import response


# Create your views here.
def register(request):
    return render(request,'login.html')
