from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    return render(request,'home.html')

def post(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def login(request):
    return render(request, 'login.html')
