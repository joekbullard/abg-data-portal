from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return TemplateResponse(request, 'index.html')