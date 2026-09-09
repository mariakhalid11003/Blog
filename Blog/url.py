from . import views
from django.urls import path

# app_name = 'Blog'

urlpatterns = [
    path('', views.home, name='home'), 
    path('posts/', views.post, name='posts'),   
    path('login/', views.login, name='login'),   
]



