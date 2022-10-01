from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook', views.Addbook),
    path('authors', views.index1),
    path('addauthor', views.Addauthor),
    path('books/<int:id>', views.bookdesc),
    path('selectauthor', views.selectonauthor),
    path('author/<int:id>', views.authordesc),
    path('selectbook', views.selectbook),

]
