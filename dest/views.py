from django.shortcuts import render , get_object_or_404
from travello.models import  Destination
# Create your views here.
def dest(request, place_name):
    print('hello')
    place = get_object_or_404(Destination, name=place_name)
    places = Destination.objects.all()
    context = {
        'place_name': place.name,
        'place_img_url': place.img.url,
        'place_description': place.description,
        'place_price': place.price,
        'places':places
    }
    return render(request,'dest.html',context)