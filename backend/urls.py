from django.contrib.auth.views import login, logout
from django.http import HttpResponse, JsonResponse
from django.urls import path
from django.utils import timezone
from django.views.generic import TemplateView


def time(request):
    if request.user.is_authenticated:
        return JsonResponse({'now': timezone.now()})
    return HttpResponse(status=401)


urlpatterns = [
    path(
        'login/',
        login,
        name='login',
    ),
    path(
        'logout/',
        logout,
        name='logout',
    ),
    path(
        'time/',
        time,
        name='time',
    ),
    path(
        'sw.js',
        TemplateView.as_view(template_name="sw.js", content_type='application/javascript'),
        name='sw.js',
    ),
    path(
        'manifest.json',
        TemplateView.as_view(template_name="manifest.json", content_type='application/manifest+json'),
        name='manifest',
    ),
    path(
        '',
        TemplateView.as_view(template_name='app.html'),
    ),
]
