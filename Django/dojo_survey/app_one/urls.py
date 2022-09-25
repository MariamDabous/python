from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('result', views.result_show),
    path('result2', views.result2_show),
]