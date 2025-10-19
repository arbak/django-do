#!/usr/bin/env python
"""
Script to create a superuser for Django app.
This can be used during deployment or for initial setup.
"""

import os
import sys
import django
from django.contrib.auth import get_user_model

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

User = get_user_model()

def create_superuser():
    """Create a superuser if one doesn't exist."""
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
    
    if User.objects.filter(username=username).exists():
        print(f"Superuser '{username}' already exists.")
        return
    
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully!")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print("Please change the password after first login!")

if __name__ == '__main__':
    create_superuser()
