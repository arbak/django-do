#!/bin/bash

# Deployment script for DigitalOcean App Platform
# This script helps with the deployment process

set -e

echo "🚀 Django App Deployment Script"
echo "================================"

# Check if doctl is installed
if ! command -v doctl &> /dev/null; then
    echo "❌ doctl is not installed. Please install it first:"
    echo "   curl -sL https://github.com/digitalocean/doctl/releases/download/v1.94.0/doctl-1.94.0-linux-amd64.tar.gz | tar -xzv"
    echo "   sudo mv doctl /usr/local/bin"
    exit 1
fi

# Check if user is authenticated
if ! doctl account get &> /dev/null; then
    echo "❌ Not authenticated with DigitalOcean. Please run:"
    echo "   doctl auth init"
    exit 1
fi

echo "✅ DigitalOcean CLI is ready"

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from .env.example..."
    cp .env.example .env
    echo "📝 Please edit .env file with your settings before continuing"
    echo "   nano .env"
    read -p "Press Enter when you've updated the .env file..."
fi

# Generate secret key if not set
if ! grep -q "SECRET_KEY=" .env || grep -q "your-secret-key-here" .env; then
    echo "🔑 Generating new SECRET_KEY..."
    SECRET_KEY=$(python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
    sed -i "s/SECRET_KEY=.*/SECRET_KEY=$SECRET_KEY/" .env
    echo "✅ SECRET_KEY generated and updated"
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser
echo "👤 Creating superuser..."
python create_superuser.py

echo ""
echo "🎉 Local setup complete!"
echo ""
echo "To deploy to DigitalOcean App Platform:"
echo "1. Push your code to GitHub:"
echo "   git init"
echo "   git add ."
echo "   git commit -m 'Initial Django app'"
echo "   git remote add origin https://github.com/your-username/your-repo.git"
echo "   git push -u origin main"
echo ""
echo "2. Deploy using doctl:"
echo "   doctl apps create --spec .do/app.yaml"
echo ""
echo "3. Or use the DigitalOcean web interface to connect your GitHub repo"
echo ""
echo "🔗 Your app will be available at: https://your-app-name.ondigitalocean.app"
echo "🔗 Admin interface: https://your-app-name.ondigitalocean.app/admin"
echo ""
echo "Default admin credentials:"
echo "Username: admin"
echo "Password: admin123"
echo "⚠️  Please change the password after first login!"
