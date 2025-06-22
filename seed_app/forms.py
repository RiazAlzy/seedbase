from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Seed

# This form is for user registration
class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

# This form is for uploading a new seed
class SeedUploadForm(forms.ModelForm):
    class Meta:
        model = Seed
        fields = '__all__'
        exclude = ['user']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('user', None)
        widgets = {
            # Add placeholders to guide the user
            'seed_text': forms.TextInput(attrs={'placeholder': 'e.g., 123456789'}),
            'spawn': forms.TextInput(attrs={'placeholder': 'spawn in plains biome on top of a woodland mansion'}),
            'cherry_grove_distance': forms.NumberInput(attrs={'placeholder': 'Distance from spawn'}),
            'cherry_grove_coords': forms.TextInput(attrs={'placeholder': 'X, Y, Z'}),
            'pale_garden_distance': forms.NumberInput(attrs={'placeholder': 'Distance from spawn'}),
            'pale_garden_coords': forms.TextInput(attrs={'placeholder': 'X, Y, Z'}),
            'mangrove_swamp_distance': forms.NumberInput(attrs={'placeholder': 'Distance from spawn'}),
            'mangrove_swamp_coords': forms.TextInput(attrs={'placeholder': 'X, Y, Z'}),
            'mansion_distance': forms.NumberInput(attrs={'placeholder': 'Distance from spawn'}),
            'mansion_coords': forms.TextInput(attrs={'placeholder': 'X, Y, Z'}),
            'monument_distance': forms.NumberInput(attrs={'placeholder': 'Distance from spawn'}),
            'monument_coords': forms.TextInput(attrs={'placeholder': 'X, Y, Z'}),
            'ancient_city_distance': forms.NumberInput(attrs={'placeholder': 'Distance from spawn'}),
            'ancient_city_coords': forms.TextInput(attrs={'placeholder': 'X, Y, Z'}),
            'desert_temple_distance': forms.NumberInput(attrs={'placeholder': 'Distance from spawn'}),
            'desert_temple_coords': forms.TextInput(attrs={'placeholder': 'X, Y, Z'}),
        }


# This form is for searching/filtering existing seeds
class SeedSearchForm(forms.Form):
    # We only care about the max distance for each structure.
    # required=False allows users to search for just one or two structures.
    max_cherry_grove = forms.IntegerField(label="Max Cherry Grove Distance", required=False)
    max_pale_garden = forms.IntegerField(label="Max Pale Garden Distance", required=False)
    max_mangrove_swamp = forms.IntegerField(label="Max Mangrove Swamp Distance", required=False)
    max_mansion = forms.IntegerField(label="Max Mansion Distance", required=False)
    max_monument = forms.IntegerField(label="Max Ocean Monument Distance", required=False)
    max_ancient_city = forms.IntegerField(label="Max Ancient City Distance", required=False)
    max_desert_temple = forms.IntegerField(label="Max Desert Temple Distance", required=False)