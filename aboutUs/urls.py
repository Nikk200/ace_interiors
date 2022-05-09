from django.contrib import admin
from django.urls import path
from . import views

def app_name(model):
    return model._meta.app_label

    
app_name = 'aboutUs'
urlpatterns = [
    path('',views.aboutUs,name='aboutUs'),
]

