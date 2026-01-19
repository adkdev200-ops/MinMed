from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
import time
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from users.models import Post, PostImage, Comments, ExtraUserInfo
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


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

@login_required
def like_post(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')  # <-- use same key as AJAX
        post = get_object_or_404(Post, id=post_id)

        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        return JsonResponse({
            "liked": liked,
            "total_likes": post.likes.count()
        })
    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required
def profile(request, username):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'userpage.html', {"posts" : posts})

@login_required
def add_comment(request):
    print('hello world')
    if request.method == 'POST':
        content = request.POST.get('content')
        post_id = request.POST.get('post_id')
        print(post_id)
        if not content:
            return JsonResponse({'error': 'Empty comment'}, status=400)

        post = get_object_or_404(Post, id=post_id)

        comment = Comments.objects.create(
            post=post,
            user=request.user,
            content=content
        )

        return JsonResponse({
            'content': comment.content,
            'user': comment.user.get_full_name() or comment.user.username,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
        })


def update_info(request):

    if request.method == 'POST':
        user = request.user
        try:
            extra_info = user.extrauserinfo
        except ObjectDoesNotExist:
            extra_info = None
        if not extra_info:
            extra_info = ExtraUserInfo.objects.create(user = user)
        user.username = request.POST.get('username')
        user.first_name= request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        extra_info.bio = request.POST.get('bio')
        if 'profile_pic' in request.FILES:
            extra_info.profile_pic = request.FILES.get('profile_pic')
        user.save()
        extra_info.save()
        
    return render(request, 'updateinfo.html')