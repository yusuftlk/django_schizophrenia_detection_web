from django.urls import path
from schizophrenia import views


urlpatterns = [  
    path('', views.index, name="index"), 
    path('list', views.list, name="list"), 
    path('add', views.add, name="add"),
    #path('ayrintilar', views.ayrintilar, name="ayrintilar"),
    path('ayrintilar/<int:hasta_id>', views.ayrintilar, name="ayrintilar"),
    path('login', views.login , name="login"),
    path('register', views.register, name="register")
]