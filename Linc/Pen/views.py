from django.shortcuts import render
from .models import Penvarity
from django.shortcuts import get_list_or_404,get_object_or_404
# Create your views here.


def info(request):
    pens=Penvarity.objects.all() # fetch all data in database
    return render(request,'Pen/info.html',{'pens':pens})


def pen_details(request,pen_id):
    pen = get_object_or_404(Penvarity,pk=pen_id)
    return render(request,'Pen/404.html',{'pen':pen})