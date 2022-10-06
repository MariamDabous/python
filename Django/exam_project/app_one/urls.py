from django.urls import path     
from . import views
urlpatterns = [
    path('', views.register_index),
    path('dashboard', views.login_index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('new/tree', views.treeform_index),
    path('plant', views.creat_Tree),
    path('user/account', views.mytree_index),
    path('delete/<int:treeid>', views.delete),
    path('update/<int:treeid>', views.edit),
    path('edit/<int:treeid>', views.edit_index),
    path('show/<int:treeid>', views.show_index),

]