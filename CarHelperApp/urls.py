from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-vehicle/', views.add_vehicle, name='add_vehicle'),
    path('create-post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('rate/<int:vehicle_id>/', views.rate_vehicle, name='rate_vehicle'),
    path('lookup/', views.vehicle_lookup, name='vehicle_lookup'),
    path('issues/', views.issue_tracker, name='issue_tracker'),
    path('delete-vehicle/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
]