from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addninja', views.addninja),
    path('adddojo', views.adddojo),
]
