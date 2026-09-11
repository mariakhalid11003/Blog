from . import views
from django.urls import path

# app_name = 'Blog'

urlpatterns = [
    path('', views.home, name='home'), 
    path('posts/', views.post, name='posts'), 
    path('create_post/', views.createpost, name='create_post'), 
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'), 
]



