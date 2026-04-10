from django import forms
from .models import Vehicle, Post

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'vin']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['vehicle', 'title', 'description']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['vehicle'].queryset = Vehicle.objects.filter(owner=user)
