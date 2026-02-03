from django.contrib.gis import admin
from box_checks.models import Site, Box, Inspection, Survey

admin.site.register(Box, admin.GISModelAdmin)
admin.site.register(Inspection, admin.ModelAdmin)
admin.site.register(Site, admin.GISModelAdmin)
admin.site.register(Survey, admin.ModelAdmin)

