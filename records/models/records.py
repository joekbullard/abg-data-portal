from django.contrib.gis.db import models
from records.models.taxonomy import Taxon
from django.conf import settings


class Record(models.Model):
    """
    This model represents the authoritative record for an observation,
    which may optionally be referenced by multiple surveys or exist
    without any survey association.
    """ 
    ABG = "ABG"
    BRERC = "BRERC"
    NBN = "NBN"
    OTHER = "OTHER"

    SOURCE_CHOICES = {
        ABG: "Avon Bat Group",
        BRERC: "BRERC",
        NBN: "NBN",
        OTHER: "Other"
    }

    id = models.UUIDField(primary_key=True)
    source_id = models.CharField(max_length=40, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    recorded_on = models.DateField()
    species = models.ForeignKey(to=Taxon, related_name="records", on_delete=models.PROTECT)
    imported_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name="records", on_delete=models.PROTECT)
    recorded_by = models.TextField()
    source = models.CharField(max_length=8, choices=SOURCE_CHOICES)
    notes = models.TextField()
    geom = models.PointField(srid=27700)

    class Meta:
        unique_together = ["source", "source_id"]
        ordering = ["-created"]