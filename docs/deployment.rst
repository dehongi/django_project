Deployment
==========

This section covers the deployment of your Django Project Template to various production environments.

Preparing for Deployment
-----------------------

Before deploying your Django project to production, you should take the following steps:

1. **Secret Key Management**:
   
   Replace the development secret key with a secure production key. Never store this key in version control.

   .. code-block:: python

       # settings.py
       SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-development-key')

2. **Debug Mode**:
   
   Disable debug mode in production:

   .. code-block:: python

       # settings.py
       DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

3. **Allowed Hosts**:
   
   Configure the allowed hosts for your application:

   .. code-block:: python

       # settings.py
       ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

4. **Database Configuration**:
   
   Use a production-ready database (PostgreSQL recommended) and configure it securely:

   .. code-block:: python

       # settings.py
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.postgresql',
               'NAME': os.environ.get('DB_NAME', 'mydatabase'),
               'USER': os.environ.get('DB_USER', 'myuser'),
               'PASSWORD': os.environ.get('DB_PASSWORD', 'mypassword'),
               'HOST': os.environ.get('DB_HOST', 'localhost'),
               'PORT': os.environ.get('DB_PORT', '5432'),
           }
       }

5. **Static and Media Files**:
   
   Configure your static and media files for production:

   .. code-block:: python

       # settings.py
       STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
       MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

       # Then run:
       # python manage.py collectstatic

6. **HTTPS Settings**:
   
   Enable HTTPS-related settings:

   .. code-block:: python

       # settings.py
       SECURE_SSL_REDIRECT = True
       SESSION_COOKIE_SECURE = True
       CSRF_COOKIE_SECURE = True
       SECURE_HSTS_SECONDS = 31536000  # 1 year
       SECURE_HSTS_INCLUDE_SUBDOMAINS = True
       SECURE_HSTS_PRELOAD = True

Deployment Options
----------------

Here are several common deployment options for Django applications:

Heroku Deployment
^^^^^^^^^^^^^^

Heroku is a popular platform for deploying Django applications:

1. Create a `Procfile` at the root of your project:

   .. code-block:: text

       web: gunicorn myproject.wsgi --log-file -

2. Create a `requirements.txt` file with all your dependencies:

   .. code-block:: text

       pip freeze > requirements.txt

3. Add `django-heroku` to your requirements and settings:

   .. code-block:: python

       # settings.py
       import django_heroku
       django_heroku.settings(locals())

4. Deploy to Heroku:

   .. code-block:: bash

       git init
       git add .
       git commit -m "Initial commit"
       heroku create
       git push heroku master
       heroku run python manage.py migrate
       heroku open

Docker Deployment
^^^^^^^^^^^^^

Docker provides a consistent deployment environment:

1. Create a `Dockerfile` at the root of your project:

   .. code-block:: dockerfile

       FROM python:3.10-slim

       WORKDIR /app

       COPY requirements.txt .
       RUN pip install --no-cache-dir -r requirements.txt

       COPY . .

       RUN python manage.py collectstatic --noinput

       EXPOSE 8000

       CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi"]

2. Create a `docker-compose.yml` file for local development:

   .. code-block:: yaml

       version: '3'
       
       services:
         web:
           build: .
           command: python manage.py runserver 0.0.0.0:8000
           volumes:
             - .:/app
           ports:
             - "8000:8000"
           depends_on:
             - db
         db:
           image: postgres:13
           environment:
             - POSTGRES_PASSWORD=postgres
             - POSTGRES_USER=postgres
             - POSTGRES_DB=postgres

3. Build and run your Docker container:

   .. code-block:: bash

       docker-compose up --build

VPS/Traditional Hosting
^^^^^^^^^^^^^^^^^^^^

For more control, you can deploy to a VPS:

1. Set up a server with Nginx and Gunicorn:

   .. code-block:: bash

       # Install required packages
       sudo apt-get update
       sudo apt-get install python3-pip python3-dev nginx
       
       # Create a virtual environment
       python3 -m venv env
       source env/bin/activate
       
       # Install dependencies
       pip install -r requirements.txt gunicorn

2. Configure Gunicorn:

   Create a systemd service file `/etc/systemd/system/gunicorn.service`:

   .. code-block:: ini

       [Unit]
       Description=gunicorn daemon
       After=network.target
       
       [Service]
       User=username
       Group=www-data
       WorkingDirectory=/path/to/your/project
       ExecStart=/path/to/your/project/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/path/to/your/project/myproject.sock myproject.wsgi:application
       
       [Install]
       WantedBy=multi-user.target

3. Configure Nginx:

   Create an Nginx site configuration at `/etc/nginx/sites-available/myproject`:

   .. code-block:: nginx

       server {
           listen 80;
           server_name yourdomain.com;
       
           location = /favicon.ico { access_log off; log_not_found off; }
           location /static/ {
               root /path/to/your/project;
           }
       
           location /media/ {
               root /path/to/your/project;
           }
       
           location / {
               include proxy_params;
               proxy_pass http://unix:/path/to/your/project/myproject.sock;
           }
       }

4. Enable the site and restart services:

   .. code-block:: bash

       sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
       sudo systemctl restart nginx
       sudo systemctl start gunicorn
       sudo systemctl enable gunicorn

Production Checklist
------------------

Before going live, ensure you've checked the following:

1. **Security Settings**:
   
   - Debug mode is off
   - Secret key is secure
   - HTTPS is configured
   - Database credentials are secure
   - ALLOWED_HOSTS is properly configured

2. **Performance Optimization**:
   
   - Static files are compressed and cached
   - Database queries are optimized
   - Consider adding caching (Redis or Memcached)

3. **Monitoring and Logging**:
   
   - Set up error monitoring (Sentry recommended)
   - Configure proper logging
   - Set up performance monitoring

4. **Backup Strategy**:
   
   - Regular database backups
   - Automated backup testing

5. **Scaling Considerations**:
   
   - Load balancing if needed
   - Database scaling plan

Continuous Deployment
-------------------

Setting up CI/CD can streamline your deployment process:

1. **GitHub Actions Example**:

   Create a `.github/workflows/deploy.yml` file:

   .. code-block:: yaml

       name: Deploy to Production
       
       on:
         push:
           branches: [ main ]
       
       jobs:
         deploy:
           runs-on: ubuntu-latest
           steps:
           - uses: actions/checkout@v2
           
           - name: Set up Python
             uses: actions/setup-python@v2
             with:
               python-version: '3.10'
               
           - name: Install dependencies
             run: |
               python -m pip install --upgrade pip
               pip install -r requirements.txt
               
           - name: Run tests
             run: |
               python manage.py test
               
           - name: Deploy to production
             if: success()
             # Add your deployment script here
             run: |
               echo "Deploying to production..." 