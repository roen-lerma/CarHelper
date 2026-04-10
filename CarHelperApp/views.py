# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import Vehicle, Post
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm, PostForm


@login_required
def home(request):
    vehicles = Vehicle.objects.filter(owner=request.user)
    # Post.objects.filter(author+request.user) is for current user feed, will change to Post.objects.all() once bulletin board is created
    posts = Post.objects.filter(author=request.user).order_by('-created_at')[:5]

    return render(request, 'CarHelperApp/home.html', {
        'vehicles': vehicles,
        'posts': posts
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # change later
    else:
        form = UserCreationForm()
    return render(request, 'CarHelperApp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'CarHelperApp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.owner = request.user
            vehicle.save()
            return redirect('home')
    else:
        form = VehicleForm()

    return render(request, 'CarHelperApp/add_vehicle.html', {
        'form': form
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm(user=request.user)

    return render(request, 'CarHelperApp/create_post.html', {
        'form': form
    })

