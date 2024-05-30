from django.urls import path

from . import  views

urlpatterns =[
    path("mumbai",views.mumbai,name="mumbai"),
    path("banglore",views.banglore,name="banglore"),
    path("pune",views.pune,name="pune"),
    path("kolkata",views.kolkata,name="kolkata"),
    path("delhi",views.delhi,name="delhi"),
    path("surat",views.surat,name="surat"),
    path('destinations/<str:place_name>/',views.destination,name="destination"),
    
]