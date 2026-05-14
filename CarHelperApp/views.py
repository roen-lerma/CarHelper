# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Vehicle, Post, Comment, Rating
from .forms import VehicleForm, PostForm, CommentForm, RatingForm
import requests

@login_required
def home(request):
    vehicles = Vehicle.objects.filter(owner=request.user)
    
    tag_filter = request.GET.get('tag', '')
    
    if tag_filter:
        posts = Post.objects.filter(tag=tag_filter).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    return render(request, 'CarHelperApp/home.html', {
        'vehicles': vehicles,
        'posts': posts,
        'tag_filter': tag_filter
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
        form = VehicleForm(request.POST, request.FILES)
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

@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.all().order_by('created_at')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'CarHelperApp/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

@login_required
def rate_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    existing_rating = Rating.objects.filter(user=request.user, vehicle=vehicle).first()

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=existing_rating)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.vehicle = vehicle
            rating.save()
            return redirect('home')
    else:
        form = RatingForm(instance=existing_rating)

    return render(request, 'CarHelperApp/rate_vehicle.html', {
        'form': form,
        'vehicle': vehicle,
        'existing_rating': existing_rating
    })

@login_required
def issue_tracker(request):
    from django.db.models import Count

    posts = Post.objects.values(
        'vehicle__make',
        'vehicle__model',
        'vehicle__year',
        'tag'
    ).annotate(
        count=Count('id')
    ).order_by('-count')

    return render(request, 'CarHelperApp/issue_tracker.html', {
        'posts': posts
    })

@login_required
def delete_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id, owner=request.user)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('home')
    return redirect('home')

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return redirect('home')

def vehicle_lookup(request):
    vehicle_data = None
    error = None

    if request.method == 'POST':
        vin = request.POST.get('vin', '').strip()
        if vin:
            try:
                url = f'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json'
                response = requests.get(url)
                data = response.json()

                results = data.get('Results', [])
                filtered = {item['Variable']: item['Value'] for item in results if item['Value'] and item['Value'] != 'Not Applicable'}

                vehicle_data = {
                    'Make': filtered.get('Make', 'N/A'),
                    'Model': filtered.get('Model', 'N/A'),
                    'Year': filtered.get('Model Year', 'N/A'),
                    'Engine': filtered.get('Displacement (L)', 'N/A'),
                    'Fuel_Type': filtered.get('Fuel Type - Primary', 'N/A'),
                    'Transmission': filtered.get('Transmission Style', 'N/A'),
                    'Drive_Type': filtered.get('Drive Type', 'N/A'),
                    'Cylinders': filtered.get('Engine Number of Cylinders', 'N/A'),
                    'Vehicle_Type': filtered.get('Vehicle Type', 'N/A'),
                }
            except Exception as e:
                error = 'Could not retrieve vehicle data. Please check the VIN and try again.'

    return render(request, 'CarHelperApp/vehicle_lookup.html', {
        'vehicle_data': vehicle_data,
        'error': error
    })