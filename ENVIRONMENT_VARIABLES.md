# Environment Variables Documentation

This document describes all the environment variables used in the Django application.

## Required Variables

### Django Core Settings

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `SECRET_KEY` | Django secret key for cryptographic signing | `django-insecure-...` | ✅ Yes |
| `DEBUG` | Enable/disable debug mode | `True` or `False` | ✅ Yes |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames | `localhost,127.0.0.1,*.ondigitalocean.app` | ✅ Yes |
| `DJANGO_SETTINGS_MODULE` | Django settings module path | `myproject.settings` | ✅ Yes |

### Database Configuration

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `DATABASE_URL` | Database connection URL | `sqlite:///db.sqlite3` | ✅ Yes |

### Subpath Configuration

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `FORCE_SCRIPT_NAME` | Base path for Django app (for subpath deployment) | `/manager` | ✅ Yes |

### CSRF and Security

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `CSRF_TRUSTED_ORIGINS` | Comma-separated list of trusted origins for CSRF | `https://app.ondigitalocean.app` | ✅ Yes |

## Optional Variables

### Superuser Configuration

| Variable | Description | Example | Default |
|----------|-------------|---------|---------|
| `DJANGO_SUPERUSER_USERNAME` | Admin username | `admin` | `admin` |
| `DJANGO_SUPERUSER_EMAIL` | Admin email | `admin@example.com` | `admin@example.com` |
| `DJANGO_SUPERUSER_PASSWORD` | Admin password | `admin123` | `admin123` |

### Static Files

| Variable | Description | Example | Default |
|----------|-------------|---------|---------|
| `STATIC_URL` | URL prefix for static files | `/static/` | `/static/` |
| `STATIC_ROOT` | Directory for collected static files | `staticfiles` | `staticfiles` |

### Server Configuration

| Variable | Description | Example | Default |
|----------|-------------|---------|---------|
| `PORT` | Port number for the application | `8080` | `8080` |

### SSL and Security

| Variable | Description | Example | Default |
|----------|-------------|---------|---------|
| `SECURE_PROXY_SSL_HEADER` | SSL header for proxy setups | `HTTP_X_FORWARDED_PROTO,https` | `HTTP_X_FORWARDED_PROTO,https` |
| `SECURE_SSL_REDIRECT` | Enable SSL redirect | `False` | `False` |

## Environment-Specific Configurations

### Local Development

```bash
# .env for local development
SECRET_KEY=django-insecure-local-development-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
FORCE_SCRIPT_NAME=
CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin123
```

### Production (DigitalOcean)

```bash
# .env for production
SECRET_KEY=your-secure-production-secret-key
DEBUG=False
ALLOWED_HOSTS=*.ondigitalocean.app,your-app-name.ondigitalocean.app
DATABASE_URL=sqlite:///db.sqlite3
FORCE_SCRIPT_NAME=/manager
CSRF_TRUSTED_ORIGINS=https://your-app-name.ondigitalocean.app,https://*.ondigitalocean.app
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=your-secure-password
```

## DigitalOcean App Platform Configuration

When deploying to DigitalOcean App Platform, these variables are set in the app spec:

```yaml
envs:
- key: SECRET_KEY
  scope: RUN_AND_BUILD_TIME
  value: your-secret-key
- key: DEBUG
  scope: RUN_AND_BUILD_TIME
  value: "False"
- key: ALLOWED_HOSTS
  scope: RUN_AND_BUILD_TIME
  value: "*.ondigitalocean.app"
- key: FORCE_SCRIPT_NAME
  scope: RUN_AND_BUILD_TIME
  value: "/manager"
- key: CSRF_TRUSTED_ORIGINS
  scope: RUN_AND_BUILD_TIME
  value: "https://your-app.ondigitalocean.app"
```

## Security Notes

1. **SECRET_KEY**: Generate a new secret key for production:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **DEBUG**: Always set to `False` in production

3. **ALLOWED_HOSTS**: Only include trusted domains

4. **CSRF_TRUSTED_ORIGINS**: Include all domains that will access your app

5. **DJANGO_SUPERUSER_PASSWORD**: Use a strong password in production

## Troubleshooting

### Common Issues

1. **CSRF Error**: Check `CSRF_TRUSTED_ORIGINS` includes your domain
2. **Host Not Allowed**: Check `ALLOWED_HOSTS` includes your domain
3. **Static Files 404**: Ensure `STATIC_ROOT` is set correctly
4. **Admin Not Accessible**: Check `FORCE_SCRIPT_NAME` matches your routing

### Environment Variable Validation

You can test your environment variables with:

```bash
python manage.py check --deploy
```

This will validate your Django configuration for production deployment.
