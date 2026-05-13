from django import forms
from .models import Vehicle, Post, Comment, Rating
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'vin']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['vehicle', 'title', 'description', 'tag']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['vehicle'].queryset = Vehicle.objects.filter(owner=user)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['reliability', 'cost_of_ownership', 'repairability', 'fuel_efficiency', 'parts_availability', 'diy_capability', 'resale_value']
        widgets = {
            'reliability': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'cost_of_ownership': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'repairability': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'fuel_efficiency': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'parts_availability': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'diy_capability': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'resale_value': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }