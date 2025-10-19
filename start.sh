#!/bin/bash

# Startup script for DigitalOcean App Platform
set -e

echo "🚀 Starting Django application..."

# Run database migrations
echo "📊 Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
echo "👤 Creating superuser..."
python manage.py create_superuser_auto

# Start the application
echo "🌐 Starting Gunicorn server on port ${PORT:-8080}..."
exec gunicorn --bind 0.0.0.0:${PORT:-8080} myproject.wsgi:application
