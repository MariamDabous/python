from django.urls import path     
from . import views
urlpatterns = [
    path('', views.register_index),
    path('wall', views.login_index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('postmessage', views.postmessage),
    path('postcomment', views.postcomment),
    
]