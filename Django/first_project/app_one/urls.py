from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.root_method),
    path('blogs/', views.index),
    path('blogs/new/',views.new_method),
    path('blogs/create/',views.create_method),
    path('blogs/<int:number>', views.show_method), 
    path('blogs/<int:number>/edit', views.edit_method),
    path('blogs/<int:number>/delete', views.destroy_method),

]