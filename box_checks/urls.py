from django.urls import path, include
from box_checks import views

urlpatterns = [
    path('new/', views.create_site, name="site_new"),
    path('site/<pk>', views.site_detail, name="site_detail")
]