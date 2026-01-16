from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import time
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from users.models import Post, PostImage

def base_page(request):
    return render(request, 'base.html')


def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)
        if user.exists():
            return HttpResponse("Username already exists")
            time.sleep(3)
            return redirect( 'signup')
        else:

            user = User.objects.create_user(first_name = first_name, last_name =  last_name, email=email, username=username )
            user.set_password(password)
            user.save()
    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        username  = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is None:
          
            
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')
    
    return render(request, 'signin.html')

@login_required
def home_page(request):
    posts  = Post.objects.all()

    return render(request, 'index.html', {'posts' : posts})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def upload_page(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        images = request.FILES.getlist('images')
        user = request.user
        post = Post.objects.create(user = user, caption = caption)
        for image in images:
            PostImage.objects.create(post = post, image = image)

    return render(request, 'upload.html')
