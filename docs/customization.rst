Customization
=============

This guide will help you customize the Django Project Template to fit your specific project requirements.

Project Settings
--------------

The main settings file is located at ``django_project/settings.py``. Here are some key settings you might want to customize:

Project Name and Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Change the project name, description, and other metadata in the settings file:

.. code-block:: python

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-this-in-production')

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

Database Configuration
^^^^^^^^^^^^^^^^^^^^

By default, the template uses SQLite. For production, you might want to switch to PostgreSQL, MySQL, or another database:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'yourdatabase',
            'USER': 'youruser',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

Remember to install the appropriate database adapter (e.g., ``psycopg2-binary`` for PostgreSQL) by adding it to your ``requirements.txt`` file.

Email Configuration
^^^^^^^^^^^^^^^^^

For production, configure proper email settings:

.. code-block:: python

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.yourmailserver.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'youremail@example.com'
    EMAIL_HOST_PASSWORD = 'yourpassword'
    DEFAULT_FROM_EMAIL = 'Your Project <noreply@yourproject.com>'

For development, you might want to use the console backend that prints emails to the console:

.. code-block:: python

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Installed Apps
^^^^^^^^^^^^

Add or remove apps as needed:

.. code-block:: python

    INSTALLED_APPS = [
        # Django built-in apps
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        
        # Third-party apps
        "your_third_party_app",
        
        # Local apps
        "accounts.apps.AccountsConfig",
        "website.apps.WebsiteConfig",
        "your_new_app.apps.YourNewAppConfig",
    ]

Customizing the User Model
------------------------

The template already uses a custom user model in ``accounts/models.py``. To extend it with additional fields:

1. Add your fields to the ``CustomUser`` model:

   .. code-block:: python

       class CustomUser(AbstractUser):
           # Existing fields...
           
           # New fields
           phone_number = models.CharField(max_length=20, blank=True, null=True)
           address = models.TextField(blank=True, null=True)
           
           # ...

2. Update the admin.py file to display the new fields:

   .. code-block:: python

       @admin.register(CustomUser)
       class CustomUserAdmin(UserAdmin):
           # ...
           fieldsets = (
               # ...
               ('Additional Information', {'fields': ('bio', 'profile_picture', 'phone_number', 'address')}),
           )
           # ...

3. If needed, update the forms in ``accounts/forms.py`` to include the new fields

4. Run migrations to apply the changes:

   .. code-block:: bash

       python manage.py makemigrations
       python manage.py migrate

Customizing Templates
-------------------

The template uses Django's template inheritance system. The base template is at ``templates/base.html``, and all other templates extend from it.

Modifying the Base Template
^^^^^^^^^^^^^^^^^^^^^^^^^

To customize the base template:

1. Edit ``templates/base.html`` to change the overall layout, navigation, footer, etc.
2. The base template contains several blocks that you can override in child templates:
   - ``title``: The page title
   - ``extra_css``: For additional CSS files
   - ``content``: The main content area
   - ``extra_js``: For additional JavaScript files

Creating New Templates
^^^^^^^^^^^^^^^^^^^^

To create a new template:

1. Create a new HTML file in the appropriate app's template directory
2. Extend the base template:

   .. code-block:: html

       {% extends 'base.html' %}

       {% block title %}
         Your Page Title
       {% endblock %}

       {% block content %}
         <!-- Your content here -->
       {% endblock %}

Customizing Static Files
---------------------

CSS Customization
^^^^^^^^^^^^^^^

The main CSS file is ``website/static/css/styles.css``. You can either modify this file directly or create a new CSS file and include it in your templates.

To include a new CSS file:

1. Add the file to ``website/static/css/``
2. Include it in your template:

   .. code-block:: html

       {% block extra_css %}
         <link rel="stylesheet" href="{% static 'css/your-custom-css.css' %}">
       {% endblock %}

JavaScript Customization
^^^^^^^^^^^^^^^^^^^^^

Similarly, you can customize JavaScript by:

1. Modifying ``website/static/js/script.js``
2. Or creating a new JS file and including it:

   .. code-block:: html

       {% block extra_js %}
         <script src="{% static 'js/your-custom-js.js' %}"></script>
       {% endblock %}

Adding New Apps
------------

To add a new app to your project:

1. Create the app:

   .. code-block:: bash

       python manage.py startapp your_app_name

2. Add the app to ``INSTALLED_APPS`` in ``django_project/settings.py``
3. Create a URL configuration in ``your_app_name/urls.py``
4. Include the app's URLs in the main URL configuration (``django_project/urls.py``):

   .. code-block:: python

       urlpatterns = [
           # Existing patterns...
           path('your-path/', include('your_app_name.urls')),
       ]

5. Create your models, views, templates, etc.

Customizing Forms
--------------

The template includes custom forms for user authentication. To customize them:

1. Edit the form classes in ``accounts/forms.py``
2. Modify the form templates in ``templates/accounts/``
3. Add Bootstrap classes and validation for a consistent look and feel

If you need to create new forms:

1. Create a forms.py file in your app
2. Define your form classes
3. Use Django's form system with Bootstrap styling
4. Create templates for rendering the forms

Deployment Customization
---------------------

For deployment, you'll want to customize:

1. ``requirements.txt`` to include all your dependencies
2. Environment-specific settings
3. Static file handling for production
4. Database configuration

Consider using environment variables for sensitive settings, and look into Django's deployment checklist for a comprehensive guide on deploying Django applications securely. 