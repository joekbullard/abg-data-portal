from django.contrib.gis.db import models
from django.conf import settings

class Site(models.Model):
    name = models.TextField()
    run_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return f"{self.name}"

class Box(models.Model):
    uid = models.UUIDField(primary_key=True)
    site = models.ForeignKey(
        to=Site,
        on_delete=models.PROTECT,
        related_name="boxes")
    number = models.IntegerField()
    model = models.TextField()
    geom = models.PointField(srid=4326)
    installed_on = models.DateField()
    notes = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "boxes"
        unique_together = ["site", "number"]        
    
    def __str__(self):
        return f"{self.site.name} - {self.number}"
    

class Survey(models.Model):
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    surveyed_on = models.DateField()

    surveyed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ["site", "surveyed_on"]


class Inspection(models.Model):
    survey = models.ForeignKey(to=Survey, on_delete=models.PROTECT)
    box = models.ForeignKey(to=Box, on_delete=models.PROTECT)
    count = models.IntegerField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.box}, {self.inspected_on}" 
