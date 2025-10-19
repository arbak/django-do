from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home_static, name='home_static'),
    path('health/', views.health_check, name='health_check'),
]
