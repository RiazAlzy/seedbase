from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Seed
from .forms import SeedUploadForm, SeedSearchForm

def home_view(request):
    """Displays the home page with the two main buttons."""
    return render(request, 'home.html')

def upload_seed_view(request):
    """Handles the seed upload form."""
    if request.method == 'POST':
        form = SeedUploadForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success message
            messages.success(request, 'Seed uploaded successfully!')
            return redirect('home') # Redirect to home page after submission
    else:
        form = SeedUploadForm()

    context = {'form': form}
    return render(request, 'upload_seed.html', context)

def search_seed_view(request):
    """Handles the search form and displays filtered results."""
    form = SeedSearchForm(request.GET or None)
    # Start with all seeds
    seeds = Seed.objects.all()

    if form.is_valid():
        # Get the cleaned data from the form
        data = form.cleaned_data
        
        # This is the core filtering logic. We chain .filter() for each criteria.
        # The '__lte' lookup means 'less than or equal to'.
        if data.get('max_cherry_grove'):
            seeds = seeds.filter(cherry_grove_distance__lte=data['max_cherry_grove'])
        if data.get('max_pale_garden'):
            seeds = seeds.filter(pale_garden_distance__lte=data['max_pale_garden'])
        if data.get('max_mangrove_swamp'):
            seeds = seeds.filter(mangrove_swamp_distance__lte=data['max_mangrove_swamp'])
        if data.get('max_mansion'):
            seeds = seeds.filter(mansion_distance__lte=data['max_mansion'])
        if data.get('max_monument'):
            seeds = seeds.filter(monument_distance__lte=data['max_monument'])
        if data.get('max_ancient_city'):
            seeds = seeds.filter(ancient_city_distance__lte=data['max_ancient_city'])
        if data.get('max_desert_temple'):
            seeds = seeds.filter(desert_temple_distance__lte=data['max_desert_temple'])

    context = {
        'form': form,
        'seeds': seeds
    }
    return render(request, 'search_seed.html', context)