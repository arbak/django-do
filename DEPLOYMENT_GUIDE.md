# 🚀 DigitalOcean App Platform Deployment Guide

This guide will walk you through deploying your Django application to DigitalOcean App Platform.

## 📋 Prerequisites

- DigitalOcean account
- GitHub account
- Basic knowledge of Git

## 🛠️ Quick Start Commands

### 1. Local Setup and Testing

```bash
# Install dependencies
pip3 install -r requirements.txt

# Run migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput

# Create superuser
python3 manage.py create_superuser_auto

# Test locally
python3 manage.py runserver
```

### 2. Deploy to DigitalOcean

#### Option A: Using DigitalOcean CLI (Recommended)

```bash
# Install doctl
curl -sL https://github.com/digitalocean/doctl/releases/download/v1.94.0/doctl-1.94.0-linux-amd64.tar.gz | tar -xzv
sudo mv doctl /usr/local/bin

# Authenticate
doctl auth init

# Deploy
doctl apps create --spec .do/app.yaml
```

#### Option B: Using Web Interface

1. Push to GitHub:
```bash
git init
git add .
git commit -m "Initial Django app"
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
```

2. Go to [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)
3. Click "Create App"
4. Connect your GitHub repository
5. DigitalOcean will auto-detect Django

## 🔧 Configuration

### Environment Variables

Set these in DigitalOcean App Platform dashboard:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=*.ondigitalocean.app
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin123
```

### Generate Secret Key

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 🎯 Post-Deployment

### Access Your App

- **Homepage**: `https://your-app-name.ondigitalocean.app`
- **Admin**: `https://your-app-name.ondigitalocean.app/admin`

### Default Admin Credentials

- **Username**: `admin`
- **Password**: `admin123`

⚠️ **Important**: Change the password after first login!

## 🔍 Troubleshooting

### Static Files Not Loading
- Ensure `STATIC_ROOT` is set
- Check WhiteNoise middleware is configured
- Verify `collectstatic` was run

### Admin Access Issues
- Verify superuser was created
- Check environment variables
- Ensure `ALLOWED_HOSTS` includes your domain

### Common Errors
- **500 Error**: Check logs in DigitalOcean dashboard
- **Static Files 404**: Verify WhiteNoise configuration
- **Database Issues**: Check if migrations ran successfully

## 📁 File Structure

```
do-container/
├── .do/app.yaml              # DigitalOcean config
├── myproject/                # Django project
├── pages/                    # Custom app
├── static/                   # Static files
├── templates/                # HTML templates
├── Dockerfile               # Docker config
├── requirements.txt         # Dependencies
└── README.md               # Documentation
```

## 🎉 Success!

Your Django app is now deployed with:
- ✅ Static file handling
- ✅ Admin interface
- ✅ Production-ready configuration
- ✅ Automatic superuser creation

## 📞 Support

- [DigitalOcean App Platform Docs](https://docs.digitalocean.com/products/app-platform/)
- [Django Deployment Guide](https://docs.djangoproject.com/en/4.2/howto/deployment/)
- [WhiteNoise Documentation](https://whitenoise.readthedocs.io/)




