from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("Hello World Home page")
def home(request):
    return render(request,'home.html')


# def about(request):
#     return HttpResponse("Hello World about page")

# def contact(request):
#     return HttpResponse("Hello World contact page")
def contact(request):
    return render(request,'contact.html')

def Dashboard(request):
    
    return  render(request,'Dashboard.html')

def about(request):
    
    return  render(request,'about.html')