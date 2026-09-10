from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def post(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def createpost(request):
    if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            # Fetch your user instance (e.g., from session)
            user_id = request.session.get('user_id')
            post.author = User.objects.get(id=user_id)
            
            post.save()
            return redirect('post')  # Redirect to your posts view/URL name
        else:
            print(form.errors)  # Check terminal to see why validation failed
    else:
        form = Post_Form()

    return render(request, "create_post.html", {"form": form})
