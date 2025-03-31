Templates
=========

The Django Project Template uses Django's template system with a well-organized structure. This section explains the template organization and how to customize the templates.

Template Organization
-------------------

The templates are organized in a project-level ``templates`` directory with subdirectories for each app:

.. code-block:: text

    templates/
    ├── base.html                 # Main base template
    ├── accounts/                 # Authentication templates
    │   ├── login.html
    │   ├── signup.html
    │   ├── profile.html
    │   ├── public_profile.html
    │   ├── profile_update.html
    │   ├── password_change.html
    │   ├── password_reset.html
    │   └── ...
    └── website/                  # Website templates
        ├── home.html
        ├── about.html
        ├── contact.html
        ├── terms.html
        └── privacy.html

This organization follows Django's best practices and allows for clear separation between different parts of the application.

Base Template
-----------

The base template (``templates/base.html``) provides the common structure for all pages, including:

- HTML doctype and metadata
- CSS and JavaScript includes
- Navigation bar
- Messages display
- Main content area
- Footer

Here's a simplified version of the base template:

.. code-block:: html

    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>
          {% block title %}
            Django Project
          {% endblock %}
        </title>

        <!-- Bootstrap 5.3 CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />

        <!-- Custom styles -->
        <link rel="stylesheet" href="{% static 'css/styles.css' %}" />

        <!-- Bootstrap Icons -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css" />

        {% block extra_css %}{% endblock %}
        
        <!-- Web App Manifest -->
        <link rel="manifest" href="{% static 'manifest.json' %}" />
      </head>
      <body>
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
          <!-- Navigation content -->
        </nav>

        <!-- Messages -->
        {% if messages %}
          <div class="container mt-4">
            {% for message in messages %}
              <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>
            {% endfor %}
          </div>
        {% endif %}

        <!-- Main Content -->
        <div class="container content py-4">
          {% block content %}{% endblock %}
        </div>

        <!-- Footer -->
        <footer class="py-4 mt-5 bg-light">
          <!-- Footer content -->
        </footer>

        <!-- Bootstrap JS Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        
        <!-- Custom JavaScript -->
        <script src="{% static 'js/script.js' %}"></script>

        {% block extra_js %}{% endblock %}
      </body>
    </html>

Template Blocks
-------------

The base template defines several blocks that can be overridden in child templates:

- ``title``: For setting the page title
- ``extra_css``: For adding page-specific CSS files
- ``content``: For the main content of the page
- ``extra_js``: For adding page-specific JavaScript files

Child Templates
------------

All other templates extend the base template using Django's template inheritance:

.. code-block:: html

    {% extends 'base.html' %}

    {% block title %}
      Page Title
    {% endblock %}

    {% block content %}
      <!-- Page content -->
    {% endblock %}

Website Templates
--------------

The website app includes templates for common pages:

1. ``home.html``: Landing page with hero section and features
2. ``about.html``: About page with information about the project
3. ``contact.html``: Contact page with contact information
4. ``terms.html``: Terms of service page
5. ``privacy.html``: Privacy policy page

These templates provide a starting point for your project and can be customized as needed.

Authentication Templates
---------------------

The accounts app includes templates for authentication and user profiles:

1. User Authentication:
   - ``login.html``: Login form
   - ``signup.html``: Registration form
   - ``password_reset.html``: Password reset request form
   - ``password_reset_confirm.html``: Form to set a new password
   - ``password_change.html``: Form to change password

2. User Profiles:
   - ``profile.html``: User's own profile page
   - ``public_profile.html``: Public view of a user's profile
   - ``profile_update.html``: Form to edit profile information

Template Context Processors
-------------------------

The template uses Django's built-in context processors to make common data available to all templates:

- ``django.template.context_processors.debug``
- ``django.template.context_processors.request``
- ``django.contrib.auth.context_processors.auth``
- ``django.contrib.messages.context_processors.messages``

These are configured in ``django_project/settings.py``:

.. code-block:: python

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

Bootstrap Integration
------------------

The templates use Bootstrap 5 for styling and components:

- Responsive grid system
- Navigation components
- Form styling
- Buttons and cards
- Alerts and modals
- Icons via Bootstrap Icons

Bootstrap JavaScript components are included via the Bootstrap bundle with Popper.js.

Custom Styling
-----------

The template includes a custom CSS file (``website/static/css/styles.css``) that extends Bootstrap with project-specific styling:

- Custom colors and variables
- Typography adjustments
- Component customizations
- Responsive adaptations

Customizing Templates
------------------

To customize the templates:

1. Modify the base template for global changes:
   - Update the navigation
   - Change the footer
   - Adjust the meta tags
   - Add global scripts or styles

2. Modify individual templates for page-specific changes:
   - Update the content
   - Add or remove sections
   - Customize the layout

3. Create new templates for new pages:
   - Extend the base template
   - Define the title and content blocks
   - Add page-specific styles or scripts

Example of creating a new page:

1. Create a new template file (e.g., ``templates/website/new_page.html``):

   .. code-block:: html

       {% extends 'base.html' %}

       {% block title %}
         New Page
       {% endblock %}

       {% block content %}
         <h1>New Page</h1>
         <p>This is a new page.</p>
       {% endblock %}

2. Add a view function or class in your app's ``views.py``:

   .. code-block:: python

       def new_page(request):
           return render(request, 'website/new_page.html', {})

3. Add a URL pattern in your app's ``urls.py``:

   .. code-block:: python

       path('new-page/', views.new_page, name='new_page'),

Template Tags and Filters
----------------------

The template uses Django's built-in template tags and filters. Some commonly used ones include:

- ``{% url %}`` for generating URLs
- ``{% static %}`` for referencing static files
- ``{% if %}``, ``{% for %}`` for control flow
- ``{% block %}`` for template inheritance
- ``{{ variable|filter }}`` for variable output with filters

For example:

.. code-block:: html

    <a href="{% url 'accounts:profile' %}">Profile</a>
    <img src="{% static 'img/logo.png' %}" alt="Logo">
    
    {% if user.is_authenticated %}
      Hello, {{ user.get_full_name }}
    {% else %}
      Please <a href="{% url 'accounts:login' %}">log in</a>
    {% endif %}
    
    <ul>
      {% for item in items %}
        <li>{{ item.name|title }}</li>
      {% endfor %}
    </ul>

Messages Framework
---------------

The template integrates Django's messages framework to display notifications to users. Messages are shown in the base template inside alert components:

.. code-block:: html

    {% if messages %}
      <div class="container mt-4">
        {% for message in messages %}
          <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          </div>
        {% endfor %}
      </div>
    {% endif %}

The message tags are mapped to Bootstrap alert classes in ``django_project/settings.py``:

.. code-block:: python

    from django.contrib.messages import constants as messages

    MESSAGE_TAGS = {
        messages.DEBUG: "secondary",
        messages.INFO: "info",
        messages.SUCCESS: "success",
        messages.WARNING: "warning",
        messages.ERROR: "danger",
    } 