from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .models import Seed
from .forms import SeedUploadForm, SeedSearchForm, UserRegisterForm # Import UserRegisterForm

def home_view(request):
    """Displays the home page with the two main buttons."""
    return render(request, 'home.html')

def register_view(request):
    """Handles user registration."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log in the user after registration
            messages.success(request, 'Registration successful!')
            return redirect('home') # Redirect to home page after registration
        else:
            # Add form errors to messages if form is invalid
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context) # Render a new register.html template

def upload_seed_view(request):
    """Handles the seed upload form."""
    if request.method == 'POST':
        form = SeedUploadForm(request.POST)
        if form.is_valid():
            seed = form.save(commit=False)
            # Set the user to the currently logged-in user if available
            if request.user.is_authenticated:
                seed.user = request.user
            seed.save()
            messages.success(request, 'Seed uploaded successfully!')
            return redirect('home')
    else:
        form = SeedUploadForm()

    context = {'form': form}
    return render(request, 'upload_seed.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# ... other views ...

@login_required
def my_seeds_view(request):
    """Displays seeds uploaded by the current user."""
    seeds = Seed.objects.filter(user=request.user)
    return render(request, 'my_seeds.html', {'seeds': seeds})

from django.http import HttpResponseForbidden

def search_seed_view(request):
    """Handles the search form and displays filtered results."""
    form = SeedSearchForm(request.GET or None)
    seeds = Seed.objects.all()

    if form.is_valid():
        data = form.cleaned_data
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

    context = {'form': form, 'seeds': seeds}
    return render(request, 'search_seed.html', context)

@login_required
def update_seed_view(request, pk):
    """Allows user to update a seed they own."""
    seed = get_object_or_404(Seed, pk=pk)
    # Ensure the user owns the seed
    if seed.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this seed")
    
    if request.method == 'POST':
        form = SeedUploadForm(request.POST, instance=seed)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seed updated successfully!')
            return redirect('my_seeds')
    else:
        form = SeedUploadForm(instance=seed)

    return render(request, 'update_seed.html', {'form': form})

@login_required
def delete_seed_view(request, pk):
    """Allows user to delete a seed they own."""
    seed = get_object_or_404(Seed, pk=pk)
    # Ensure the user owns the seed
    if seed.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this seed")
    
    if request.method == 'POST':
        seed.delete()
        messages.success(request, 'Seed deleted successfully!')
        return redirect('my_seeds')
    
    return render(request, 'confirm_delete_seed.html', {'seed': seed})