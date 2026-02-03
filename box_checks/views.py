from django.shortcuts import render, redirect, get_object_or_404
from box_checks.forms import SiteForm
from django.contrib.auth.decorators import login_required
from box_checks.models import Site, Box
from django.core import serializers
from django.template.response import TemplateResponse
from django.http import HttpRequest, HttpResponse
from django.template import loader

@login_required
def create_site(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.run_by = request.user
            site.save()
            return redirect('site-detail', pk=site.pk)
    else:
        form = SiteForm()
    return render(request, 'box-checks/create-site.html', {"form":form})


@login_required
def site_detail(request:HttpRequest, pk: int) -> HttpResponse:
    site = get_object_or_404(Site, pk=pk)
    box_geojson = serializers.serialize("geojson", Box.objects.filter(site=site), geometry_field="geom", id_field="id")
    context = {"site": site, "boxes": box_geojson}
    return render(request, "box-checks/site-detail.html", context=context)