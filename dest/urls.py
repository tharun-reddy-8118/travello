from django.urls import path
from . import views

urlpatterns = [
    path('dest/<str:place_name>/',views.dest,name="dest")
    # other URL patterns
]