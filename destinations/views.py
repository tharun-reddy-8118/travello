from django.shortcuts import render , get_object_or_404
from travello.models import Place , Destination
# Create your views here.
def mumbai(request):
    return render(request,'mumbai.html')

def banglore(request):
    return render(request,'banglore.html')

def kolkata(request):
    return render(request,'kolkata.html')

def pune(request):
    return render(request,'pune.html')

def delhi(request):
    return render(request,'delhi.html')

def surat(request):
    return render(request,'surat.html')
def destination(request, place_name):
    place = get_object_or_404(Place, name=place_name)
    places = Place.objects.all()
    context = {
        'place_name': place.name,
        'place_img_url': place.img.url,
        'place_description': place.description,
        'place_price': place.price,
        'places':places
    }
    return render(request,'destination.html',context)
