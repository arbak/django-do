from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser automatically'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Superuser "{username}" already exists.')
            )
            return
        
        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created superuser "{username}"')
        )
        self.stdout.write(f'Username: {username}')
        self.stdout.write(f'Password: {password}')
        self.stdout.write('Please change the password after first login!')
