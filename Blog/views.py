from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Post
from .forms import Post_Form
# Create your views here.

def home(request):
    return render(request,'home.html')

def post(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        email=request.POST['email']

        #checks 
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('home')
        # 2. Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another one.")
            return redirect('home')

        # 3. Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('home')
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,'Your Blogs.com account has been successfully created')
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found ')

    
def login(request):
     if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']

            user=authenticate(username=username,password=password)

            if user is not None:
                auth_login(request,user)
                messages.success(request,'Successfully logged in ')
                return redirect('home')

            else:
                messages.error(request,'Invalid Credentials')
                return redirect('home')

     else:
            return HttpResponse('404 - Not Found ')


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
