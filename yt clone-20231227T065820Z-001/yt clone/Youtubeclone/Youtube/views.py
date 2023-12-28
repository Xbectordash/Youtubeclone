from django.shortcuts import render
from django.http import response

# Create your views here.
def yt(request):
    return render(request,'youtube.html')

    
