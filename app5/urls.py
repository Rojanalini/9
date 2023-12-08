from app5.views import *
from django.urls import path
app_name='anything'
 

urlpatterns=[
    path('ban/',ban,name='ban')
 ]