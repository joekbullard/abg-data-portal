from django.contrib.gis.db import models
from django.conf import settings

class Site(models.Model):
    name = models.TextField()
    run_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return f"{self.name}"


class Box(models.Model):
    uid = models.UUIDField(primary_key=True)
    site = models.ForeignKey(
        to=Site,
        on_delete=models.CASCADE)
    number = models.IntegerField()
    model = models.TextField()
    geom = models.PointField(srid=4326)
    installed_on = models.DateField()
    notes = models.TextField(null=True)

    class Meta:
        unique_together = ["site", "number"]        
    
    def __str__(self):
        return f"{self.site.name} - {self.number}"

    
class Inspection(models.Model):
    box = models.ForeignKey(to=Box, on_delete=models.CASCADE)
    inspected_on = models.DateField()
    count = models.IntegerField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.box}, {self.inspected_on}" 
