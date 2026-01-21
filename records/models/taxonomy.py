"""This contains taxonomy info for bat species"""
from django.db import models

class Taxon(models.Model):
    
    class Rank(models.TextChoices):
        SPECIES = "species", "Species"
        GENUS = "genus", "Genus"
        GROUP = "functional", "Functional"
        UNKNOWN = "unknown", "Unknown"
        
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    rank = models.TextChoices(choices=Rank.choices)
    genus = models.CharField(max_length=50)
    nbn_taxon_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.common_name}"
