from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name = 'teca-home'),
    path('help/', views.help, name = 'teca-help'),
]
