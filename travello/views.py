from django.shortcuts import render
from .models import Destination , Place , Trips
# Create your views here.
def index(request):
    dests = Destination.objects.all().order_by('-id')[:6]
    places = Place.objects.all().order_by('-id')[:6]
    trips = Trips.objects.all().order_by('-id')[:3]
    return render(request,"index.html",{'dests':dests,'places':places,'trips':trips})
def destination(request):
    places = Place.objects.all()
    return render(request,'destination.html',{'places':places})
