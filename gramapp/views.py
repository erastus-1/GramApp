from django.contrib.auth.decorators import login_required
from .models import Image, Profile,Comment,Follow,Likes
from .forms import ProfileForm,ImageForm,CommentForm
from django.contrib.auth import views as auth_views
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()
    print(likes)
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


    return render(request,'image.html',locals())

@login_required(login_url='/accounts/login/')
def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(searchs)

        return render(request,'search.html',locals())

    return redirect(home)

@login_required(login_url='/accounts/login/')
def comment(request,image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    profile_owner = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.comment_owner = current_user
            comment.save()

            print(comments)


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

