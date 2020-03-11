from django.urls import path 
from . import views 

urlpatterns=[
    path('',views.home,name="home"),
    path('home1',views.home1,name="home1"),
    path('about',views.about,name="about"),
    path('gallery',views.gallery,name="gallery"),
    path('contact',views.contact,name="contact"),

]