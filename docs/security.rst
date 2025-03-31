Security
========

This section covers the security features and best practices implemented in the Django Project Template.

Django's Security Features
------------------------

Django provides several built-in security features, and this template ensures they are properly configured:

1. **Cross-Site Scripting (XSS) Protection**:
   
   Django's template system automatically escapes variables to prevent XSS attacks:

   .. code-block:: html

       <!-- Variables are automatically escaped -->
       <p>{{ user_provided_content }}</p>
       
       <!-- If you need to render HTML safely, use the 'safe' filter only when necessary -->
       <p>{{ trusted_html|safe }}</p>

2. **Cross-Site Request Forgery (CSRF) Protection**:
   
   CSRF protection is enabled by default. Always include the CSRF token in forms:

   .. code-block:: html

       <form method="post">
           {% csrf_token %}
           {{ form.as_p }}
           <button type="submit">Submit</button>
       </form>

3. **SQL Injection Protection**:
   
   Django's ORM parameters are properly escaped to prevent SQL injection:

   .. code-block:: python

       # Safe - parameters are properly escaped
       User.objects.filter(username=username)
       
       # Avoid raw SQL when possible, but if needed:
       User.objects.raw('SELECT * FROM auth_user WHERE username = %s', [username])

4. **Clickjacking Protection**:
   
   The X-Frame-Options middleware is enabled to prevent clickjacking:

   .. code-block:: python

       # settings.py
       MIDDLEWARE = [
           'django.middleware.security.SecurityMiddleware',
           'django.middleware.clickjacking.XFrameOptionsMiddleware',
           # ...
       ]
       
       # Default is 'SAMEORIGIN'
       X_FRAME_OPTIONS = 'DENY'

Authentication Security
---------------------

The template implements secure authentication practices:

1. **Email-Based Authentication**:
   
   Using email as the primary identifier instead of username:

   .. code-block:: python

       # accounts/models.py
       class CustomUser(AbstractBaseUser, PermissionsMixin):
           email = models.EmailField(_('email address'), unique=True)
           # ...

2. **Password Hashing**:
   
   Django's password hashing system uses PBKDF2 by default:

   .. code-block:: python

       # settings.py
       PASSWORD_HASHERS = [
           'django.contrib.auth.hashers.PBKDF2PasswordHasher',
           'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
           'django.contrib.auth.hashers.Argon2PasswordHasher',
           'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
       ]

3. **Password Validation**:
   
   Password validators ensure strong passwords:

   .. code-block:: python

       # settings.py
       AUTH_PASSWORD_VALIDATORS = [
           {
               'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
           },
           {
               'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
               'OPTIONS': {
                   'min_length': 8,
               }
           },
           {
               'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
           },
           {
               'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
           },
       ]

4. **Login Throttling**:
   
   Limit login attempts to prevent brute-force attacks:

   .. code-block:: python

       # accounts/views.py
       from django.contrib.auth.views import LoginView
       from django.contrib.auth.forms import AuthenticationForm
       from django.core.cache import cache
       from django.utils import timezone
       
       class ThrottledLoginView(LoginView):
           form_class = AuthenticationForm
           template_name = 'accounts/login.html'
           
           def form_invalid(self, form):
               email = form.data.get('email', '')
               cache_key = f'login_attempts_{email}'
               login_attempts = cache.get(cache_key, 0) + 1
               cache.set(cache_key, login_attempts, 300)  # 5 minutes cooldown
               
               if login_attempts >= 5:
                   form.add_error(None, "Too many login attempts. Please try again in 5 minutes.")
               
               return super().form_invalid(form)

HTTPS Configuration
-----------------

For production environments, HTTPS should be enabled:

.. code-block:: python

    # settings.py for production
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

Content Security Policy
---------------------

Implement a Content Security Policy to mitigate XSS and other code injection attacks:

.. code-block:: python

    # settings.py
    MIDDLEWARE = [
        # ...
        'csp.middleware.CSPMiddleware',
    ]
    
    CSP_DEFAULT_SRC = ("'self'",)
    CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net")
    CSP_SCRIPT_SRC = ("'self'", "https://cdn.jsdelivr.net")
    CSP_IMG_SRC = ("'self'", "data:", "https:")
    CSP_FONT_SRC = ("'self'", "https://cdn.jsdelivr.net")

File Upload Security
------------------

Secure file uploads to prevent malicious file execution:

1. **Validate File Types**:

   .. code-block:: python

       def validate_file_extension(value):
           ext = os.path.splitext(value.name)[1]
           valid_extensions = ['.jpg', '.jpeg', '.png', '.pdf']
           if ext.lower() not in valid_extensions:
               raise ValidationError('Unsupported file extension.')

2. **Store Files Securely**:

   .. code-block:: python

       # Store uploaded files outside the document root
       MEDIA_ROOT = os.path.join(BASE_DIR, 'protected_media')
       
       # Use a separate URL pattern with permission checks
       def protected_serve(request, path, document_root=None):
           if not request.user.is_authenticated:
               raise PermissionDenied()
           return serve(request, path, document_root)

3. **Scan Uploaded Files** (optional):

   Consider integrating with a virus scanning API for uploaded files.

Database Security
--------------

Protect your database:

1. **Use Environment Variables**:

   .. code-block:: python

       # settings.py
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.postgresql',
               'NAME': os.environ.get('DB_NAME'),
               'USER': os.environ.get('DB_USER'),
               'PASSWORD': os.environ.get('DB_PASSWORD'),
               'HOST': os.environ.get('DB_HOST'),
               'PORT': os.environ.get('DB_PORT'),
           }
       }

2. **Limit Database User Permissions**:

   Grant only the permissions needed for your application to the database user.

3. **Regular Backups**:

   Implement automated, encrypted backups with periodic testing.

Security Monitoring
-----------------

Implement security monitoring:

1. **Logging**:

   .. code-block:: python

       # settings.py
       LOGGING = {
           'version': 1,
           'disable_existing_loggers': False,
           'formatters': {
               'verbose': {
                   'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                   'style': '{',
               },
           },
           'handlers': {
               'file': {
                   'level': 'WARNING',
                   'class': 'logging.FileHandler',
                   'filename': os.path.join(BASE_DIR, 'logs/django.log'),
                   'formatter': 'verbose',
               },
           },
           'loggers': {
               'django.security': {
                   'handlers': ['file'],
                   'level': 'WARNING',
                   'propagate': True,
               },
           },
       }

2. **Error Tracking**:

   Integration with Sentry for error tracking:

   .. code-block:: python

       # settings.py
       import sentry_sdk
       from sentry_sdk.integrations.django import DjangoIntegration
       
       sentry_sdk.init(
           dsn="your-sentry-dsn",
           integrations=[DjangoIntegration()],
           traces_sample_rate=0.1,
       )

Regular Security Updates
---------------------

Keep dependencies updated:

1. **Check for Vulnerabilities**:

   Regularly run security checks on dependencies:

   .. code-block:: bash

       pip install safety
       safety check

2. **Pin Dependencies**:

   Use specific versions in requirements.txt and update them regularly.

3. **Django Security Updates**:

   Subscribe to the Django security mailing list to stay informed about security updates.

Security Checklist
----------------

Before deploying to production, go through this security checklist:

1. ☐ Debug mode is turned off
2. ☐ Secret key is properly secured
3. ☐ Database credentials are stored securely
4. ☐ HTTPS is properly configured
5. ☐ CSRF protection is enabled
6. ☐ Content Security Policy is implemented
7. ☐ Password validation is enforced
8. ☐ File upload validation is in place
9. ☐ User permissions are properly configured
10. ☐ Security headers are set
11. ☐ Database backups are automated and tested
12. ☐ Logging and monitoring are configured
13. ☐ Dependencies are up-to-date and checked for vulnerabilities 