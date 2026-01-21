"""This contains taxonomy info for bat species"""
from django.db import models

class Rank(models.TextChoices):
    SPECIES = "species", "Species"
    GENUS = "genus", "Genus"
    GROUP = "functional", "Functional"
    UNKNOWN = "unknown", "Unknown"  

class Taxon(models.Model):
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    rank = models.CharField(choices=Rank.choices)
    genus = models.CharField(max_length=50)
    nbn_taxon_id = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "taxa"
    
    def __str__(self):
        return f"{self.common_name}"
    
