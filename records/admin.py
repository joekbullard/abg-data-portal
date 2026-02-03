from django.contrib.gis import admin
from records.models.taxonomy import Taxon
from records.models.records import Record

admin.site.register(Taxon, admin.ModelAdmin)
admin.site.register(Record, admin.GISModelAdmin)
