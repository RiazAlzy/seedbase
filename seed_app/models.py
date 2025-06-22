from django.db import models

class Seed(models.Model):
    # Core Details
    seed_text = models.CharField(max_length=100, unique=True, help_text="541cd55155165")
    spawn = models.CharField(max_length=500, help_text="spawn in plains biome on top of a woodland mansion")

  
    cherry_grove_distance = models.IntegerField(null=True, blank=True)
    cherry_grove_coords = models.CharField(max_length=50, null=True, blank=True)

    pale_garden_distance = models.IntegerField(null=True, blank=True)
    pale_garden_coords = models.CharField(max_length=50, null=True, blank=True)

    mangrove_swamp_distance = models.IntegerField(null=True, blank=True)
    mangrove_swamp_coords = models.CharField(max_length=50, null=True, blank=True)

    mansion_distance = models.IntegerField(null=True, blank=True)
    mansion_coords = models.CharField(max_length=50, null=True, blank=True)

    monument_distance = models.IntegerField(null=True, blank=True)
    monument_coords = models.CharField(max_length=50, null=True, blank=True)

    ancient_city_distance = models.IntegerField(null=True, blank=True)
    ancient_city_coords = models.CharField(max_length=50, null=True, blank=True)

    desert_temple_distance = models.IntegerField(null=True, blank=True)
    desert_temple_coords = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"Seed: {self.seed_text}"