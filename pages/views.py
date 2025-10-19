from django.shortcuts import render
from django.http import JsonResponse
import os


def home(request):
    """Simple home page view."""
    from django.conf import settings
    
    context = {
        'title': 'Welcome to My Django App',
        'message': 'This is a simple Django application deployed on DigitalOcean App Platform!',
    }
    
    # Only show debug information when DEBUG=True
    if settings.DEBUG:
        context['debug_info'] = {
            'debug': os.environ.get('DEBUG', 'Not set'),
            'force_script_name': os.environ.get('FORCE_SCRIPT_NAME', 'Not set'),
            'allowed_hosts': os.environ.get('ALLOWED_HOSTS', 'Not set'),
        }
    
    return render(request, 'pages/home.html', context)


def home_static(request):
    """Static home page for testing."""
    return render(request, 'pages/home_static.html')


def health_check(request):
    """Health check endpoint for DigitalOcean."""
    return JsonResponse({
        'status': 'healthy',
        'message': 'Django app is running',
        'debug': os.environ.get('DEBUG', 'Not set'),
        'force_script_name': os.environ.get('FORCE_SCRIPT_NAME', 'Not set'),
    })