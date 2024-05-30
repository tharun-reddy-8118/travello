from django.urls import path

from . import  views

urlpatterns =[
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("contact",views.contact,name="contact"),
    path("about",views.about,name="about"),
    path("trips",views.trips,name="trips"),
    path('search/', views.search_view, name='search'),
]