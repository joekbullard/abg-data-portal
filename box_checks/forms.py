from django.contrib.gis import forms as geoforms
from box_checks.models import Site

class SiteForm(geoforms.ModelForm):
    name = geoforms.CharField()
    geom = geoforms.PointField(widget=geoforms.OSMWidget(attrs={"style": "width:800px; height:500px;"}))
    
    class Meta:
        model = Site
        fields = ["name", "geom"]