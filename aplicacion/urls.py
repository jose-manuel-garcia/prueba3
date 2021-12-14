from django.urls import include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    
    path('usuario/', views.usuarios_view, name='usuarios'),
]