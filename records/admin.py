from django.contrib import admin
from records.models.taxonomy import Taxon

admin.site.register(Taxon, admin.ModelAdmin)
