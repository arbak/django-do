# Django App for DigitalOcean App Platform

A simple Django application with admin interface, ready for deployment on DigitalOcean App Platform.

## Features

- ✅ Django 4.2.7 with admin interface
- ✅ Static file handling with WhiteNoise
- ✅ Bootstrap 5 for modern UI
- ✅ Production-ready configuration
- ✅ Docker support
- ✅ DigitalOcean App Platform configuration

## Local Development

### 1. Set up the environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure environment variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file with your settings
# SECRET_KEY=your-secret-key-here
# DEBUG=True
# ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Run migrations and create superuser

```bash
# Run database migrations
python manage.py migrate

# Create a superuser account
python manage.py createsuperuser
```

### 4. Start the development server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see your app and `http://localhost:8000/admin` for the admin interface.

## Deployment to DigitalOcean App Platform

### Method 1: Using DigitalOcean CLI (Recommended)

1. **Install DigitalOcean CLI**
   ```bash
   # Install doctl
   curl -sL https://github.com/digitalocean/doctl/releases/download/v1.94.0/doctl-1.94.0-linux-amd64.tar.gz | tar -xzv
   sudo mv doctl /usr/local/bin
   
   # Authenticate
   doctl auth init
   ```

2. **Deploy the app**
   ```bash
   # Deploy using the app.yaml configuration
   doctl apps create --spec .do/app.yaml
   ```

### Method 2: Using DigitalOcean Web Interface

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial Django app"
   git branch -M main
   git remote add origin https://github.com/your-username/your-repo-name.git
   git push -u origin main
   ```

2. **Create App on DigitalOcean**
   - Go to [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)
   - Click "Create App"
   - Connect your GitHub repository
   - Select the repository and branch
   - DigitalOcean will auto-detect the Django app

3. **Configure Environment Variables**
   - In the App Platform dashboard, go to Settings → App-Level Environment Variables
   - Add the following variables:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=False
     ALLOWED_HOSTS=*.ondigitalocean.app
     ```

### Method 3: Using Docker

1. **Build and test locally**
   ```bash
   # Build the Docker image
   docker build -t django-app .
   
   # Run the container
   docker run -p 8080:8080 -e SECRET_KEY=your-secret-key django-app
   ```

2. **Deploy to DigitalOcean Container Registry**
   ```bash
   # Login to DigitalOcean Container Registry
   doctl registry login
   
   # Tag and push the image
   docker tag django-app registry.digitalocean.com/your-registry/django-app
   docker push registry.digitalocean.com/your-registry/django-app
   ```

## Post-Deployment Setup

### Create Superuser Account

After deployment, you need to create a superuser account. You can do this by:

1. **Using DigitalOcean App Platform Console**
   ```bash
   # Connect to your app's console
   doctl apps create-deployment --wait your-app-id
   
   # Run the createsuperuser command
   doctl apps run --command "python manage.py createsuperuser" your-app-id
   ```

2. **Using a management command (Alternative)**
   Create a custom management command to create a superuser automatically.

### Access Your App

- **Homepage**: `https://your-app-name.ondigitalocean.app`
- **Admin Interface**: `https://your-app-name.ondigitalocean.app/admin`

## Important Notes

### Static Files
- Static files are handled by WhiteNoise middleware
- CSS and JavaScript files are automatically served
- Files are compressed and cached for better performance

### Security
- Change the `SECRET_KEY` in production
- Set `DEBUG=False` for production
- Configure `ALLOWED_HOSTS` properly

### Database
- The app uses SQLite by default (suitable for small apps)
- For production with multiple instances, consider using PostgreSQL

## Troubleshooting

### Static Files Not Loading
- Ensure `STATIC_ROOT` is set correctly
- Run `python manage.py collectstatic` before deployment
- Check that WhiteNoise middleware is properly configured

### Admin Interface Issues
- Verify superuser account is created
- Check that `LOGIN_URL` and `LOGIN_REDIRECT_URL` are set
- Ensure `django.contrib.admin` is in `INSTALLED_APPS`

### Deployment Issues
- Check environment variables are set correctly
- Verify `ALLOWED_HOSTS` includes your domain
- Check DigitalOcean App Platform logs for errors

## File Structure

```
do-container/
├── .do/
│   └── app.yaml              # DigitalOcean App Platform config
├── myproject/
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── pages/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py              # Pages app URLs
│   └── views.py             # Home page view
├── static/
│   ├── css/
│   │   └── style.css        # Custom CSS
│   └── js/
│       └── main.js          # Custom JavaScript
├── templates/
│   ├── base.html            # Base template
│   └── pages/
│       └── home.html        # Home page template
├── .env.example             # Environment variables example
├── .gitignore
├── Dockerfile               # Docker configuration
├── manage.py
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Support

For issues with this Django app, check:
1. DigitalOcean App Platform documentation
2. Django documentation
3. WhiteNoise documentation for static file issues
