from django.shortcuts import render
from .models import Penvarity
# Create your views here.


def info(request):
    pens=Penvarity.objects.all() # fetch all data in database
    return render(request,'Pen/info.html',{'pens':pens})
