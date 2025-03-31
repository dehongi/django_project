Static Files
===========

This section covers how static files are organized and used in the Django Project Template.

Static Files Organization
------------------------

The Django Project Template follows Django's recommended approach for handling static files. Static files are organized in a project-level ``static`` directory, with subdirectories for different types of assets:

.. code-block:: text

    static/
    ├── css/
    │   ├── base.css
    │   └── custom.css
    ├── js/
    │   ├── main.js
    │   └── utilities.js
    └── images/
        ├── favicon.ico
        └── logo.png

Django Static Files Configuration
--------------------------------

The template is configured to handle static files using Django's built-in support. The following settings in ``settings.py`` manage static files:

.. code-block:: python

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]
    STATIC_ROOT = BASE_DIR / 'staticfiles'

    # Media files (User uploads)
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

CSS Framework
------------

The template uses Bootstrap 5 for styling. Bootstrap is included via CDN in the base template:

.. code-block:: html

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

Custom CSS
---------

The template includes a ``custom.css`` file for your project-specific styling. This is loaded after Bootstrap to allow overriding Bootstrap styles:

.. code-block:: html

    <!-- Custom CSS -->
    <link href="{% static 'css/custom.css' %}" rel="stylesheet">

The ``custom.css`` file is intentionally minimal to serve as a starting point for your styling.

JavaScript Files
--------------

The template includes a basic JavaScript structure:

1. **Bootstrap JS** is loaded via CDN
2. **main.js** contains site-wide JavaScript functionality
3. **utilities.js** contains reusable utility functions

.. code-block:: html

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- Custom JS -->
    <script src="{% static 'js/utilities.js' %}"></script>
    <script src="{% static 'js/main.js' %}"></script>

Including Static Files in Templates
----------------------------------

To use static files in templates, use the ``{% static %}`` template tag:

.. code-block:: html

    {% load static %}
    
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    <link href="{% static 'css/custom.css' %}" rel="stylesheet">
    <script src="{% static 'js/main.js' %}"></script>

Handling Media Files
------------------

Media files (user uploads) are separate from static files and are handled differently:

1. Media files are stored in the ``media`` directory
2. During development, Django serves media files automatically when using the development server
3. For production, you'll need to configure your web server to serve files from the ``MEDIA_ROOT``

The template includes configuration for serving media files in development:

.. code-block:: python

    # urls.py
    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns = [
        # Your URL patterns...
    ]
    
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Static Files in Production
------------------------

For production deployment, you should:

1. Run ``python manage.py collectstatic`` to collect all static files to the ``STATIC_ROOT`` directory
2. Configure your web server (Nginx, Apache, etc.) to serve files from ``STATIC_ROOT``
3. Consider using a CDN for better performance

Customizing Static Files
----------------------

To customize the static files in your project:

1. Add new CSS files to the ``static/css/`` directory
2. Add new JavaScript files to the ``static/js/`` directory
3. Update the base template to include your new files
4. Keep a clear organization by separating concerns (CSS, JS, images)
5. Consider using a CSS preprocessor like SASS for more complex projects

Best Practices
------------

1. **Minimize HTTP requests**: Combine and minify CSS and JS files for production
2. **Use versioning**: Add version parameters to file URLs to handle caching (e.g., ``style.css?v=1.2``)
3. **Optimize images**: Compress images to improve load times
4. **Lazy load**: Consider lazy loading for images and non-critical resources
5. **Use preload/prefetch**: For critical resources, use preload hints 