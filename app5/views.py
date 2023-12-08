from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ban(request):
    return HttpResponse('<center>Banglore is one cooliest city in india wich alomost 13crs population in the city</center>')