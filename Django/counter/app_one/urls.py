from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy_session/',views.destroy),
    path('increment/',views.add),
    path('increment/<int:number>',views.addnum),

]
