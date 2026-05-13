from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, blank=True, null=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Post(models.Model):
    TAG_CHOICES = [
        ('engine', 'Engine'),
        ('transmission', 'Transmission'),
        ('electrical', 'Electrical'),
        ('suspension', 'Suspension'),
        ('other', 'Other'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    reliability = models.IntegerField()
    cost_of_ownership = models.IntegerField()
    repairability = models.IntegerField()
    fuel_efficiency = models.IntegerField()
    parts_availability = models.IntegerField()
    diy_capability = models.IntegerField()
    resale_value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'vehicle')

    def __str__(self):
        return f"{self.user} rated {self.vehicle}"