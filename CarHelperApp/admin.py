from django.contrib import admin
from .models import Vehicle, Post, Comment, Rating

admin.site.register(Vehicle)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Rating)