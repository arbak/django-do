from django.shortcuts import render


def home(request):
    """Simple home page view."""
    context = {
        'title': 'Welcome to My Django App',
        'message': 'This is a simple Django application deployed on DigitalOcean App Platform!',
    }
    return render(request, 'pages/home.html', context)
