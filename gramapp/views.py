from django.contrib.auth.decorators import login_required
from .models import Image, Profile,Comment,Follow,Likes
from .forms import ProfileForm,ImageForm,CommentForm
from django.contrib.auth import views as auth_views
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()

    return render(request,'home.html',locals())

@login_required(login_url='accounts/login/')
def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request,'image.html',{"form":form})


@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.owner = current_user
            profile.save()
        return redirect('profile')
    else:
        form=ProfileForm()

    return render(request, 'profile/new.html',{"form":form})


@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    profile_details = Profile.get_by_id(id)
    images = Image.get_profile_images(id)

    usersss = User.objects.get(id=id)
    follower = len(Follow.objects.followers(usersss))
    following = len(Follow.objects.following(usersss))
    people=User.objects.all()
    pip_following=Follow.objects.following(request.user)

    return render(request,'profile/profile.html', {"images": images, "profile":profile})


@login_required(login_url='/accounts/login/')
def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        message = f'{search_term}'
        profile_pic = User.objects.all()

        return render(request,'search.html',{"message":message, 'results':searched_users, 'profile_pic':profile_pic})

    return render(request, 'search.html', {'message':message})

@login_required(login_url='/accounts/login/')
def comment(request,image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    profile_owner = User.objects.get(username=current_user.username)
    comments = Comment.objects.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.comment_owner = current_user
            comment.save()

        return redirect(home)

    else:
        form = CommentForm()

    return render(request, 'comment.html', locals())

def follow(request,user_id):
    users=User.objects.get(id=user_id)
    follow = Follow.objects.add_follower(request.user, users)

    return redirect('/profile/', locals())

def unfollow(request, user_id):
    other_user = User.objects.get(id = user_id)
    follow = Follow.objects.remove_follower(request.user, other_user)

    return redirect('home')

@login_required(login_url='/accounts/login/')
def like(request, image_id):
    current_user = request.user
    image=Image.objects.get(id=image_id)
    new_like,created= Likes.objects.get_or_create(liker=current_user, image=image)
    new_like.save()

    return redirect('home')

