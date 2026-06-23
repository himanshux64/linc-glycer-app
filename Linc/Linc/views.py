from django.http import HttpResponse
from django.shortcuts import render


def glycer(request):
    return render(request,'glycer.html')
def home(request):
    return render(request,'home.html')
def info(request):
    return render(request,'Pen/info.html')