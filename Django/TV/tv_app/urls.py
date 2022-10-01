from django.urls import path     
from . import views
urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.index2),
    path('create', views.create),
    path('shows/<int:id5>', views.index3),
    path('shows/<int:id5>/edit', views.index4),
    path('update/<int:id5>', views.update),
    path('shows/delete/<int:id4>', views.delete1),
]
