from django.contrib import admin
from .models import Seed

# A class to customize how the Seed model is displayed in the admin
class SeedAdmin(admin.ModelAdmin):
    # These are the columns that will be displayed in the list view
    list_display = ('seed_text', 'spawn', 'mansion_distance', 'ancient_city_distance')
    
    # This adds a search box to the admin page
    search_fields = ('seed_text',)

# Register model with the custom admin class
admin.site.register(Seed, SeedAdmin)