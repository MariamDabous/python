from django.urls import path     
from . import views
urlpatterns = [
    path('', views.register_index),
    path('books', views.login_index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('addbook', views.AddBook),
    path('books/<int:id>', views.oneBook_index),
    path('newdesc', views.newdesc),
    path('unfav', views.unfav),
    path('addfav/<int:id2>', views.addfav),
    path('addfavfromone/<int:id2>', views.addfav2_on_onebook_page),
    path('delete', views.delete),
    
    
]
