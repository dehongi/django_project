Getting Started
===============

This guide will walk you through the process of using the Django Project Template, from creating your repository to running your application locally.

Using the Template
-----------------

There are two ways to use this template to create your own project:

Option 1: Use GitHub's "Use this template" Feature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the recommended approach if you're using GitHub:

1. Navigate to the template repository on GitHub
2. Click the green "Use this template" button at the top of the repository page
3. Choose "Create a new repository"
4. Enter your repository name and other details
5. Click "Create repository from template"

This will create a new repository with all the files from the template, but without the commit history.

Option 2: Clone and Reinitialize
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you prefer to start from scratch or don't use GitHub:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/yourusername/django_project.git your-project-name
      cd your-project-name

2. Remove the existing git history and start fresh:

   .. code-block:: bash

      rm -rf .git
      git init
      git add .
      git commit -m "Initial commit from template"

Setting Up the Environment
-------------------------

Once you have your project repository, follow these steps to set up your development environment:

1. Create a virtual environment:

   .. code-block:: bash

      python -m venv .venv

2. Activate the virtual environment:

   **On Linux/macOS**:

   .. code-block:: bash

      source .venv/bin/activate

   **On Windows**:

   .. code-block:: bash

      .venv\Scripts\activate

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

Database Setup
-------------

The template uses SQLite by default, which is perfect for development. To set up the database:

1. Apply migrations to create the database schema:

   .. code-block:: bash

      python manage.py migrate

2. Create a superuser (admin) account:

   .. code-block:: bash

      python manage.py createsuperuser

   Follow the prompts to create your admin user. Since the template uses email authentication, you'll need to provide a valid email address.

Running the Development Server
-----------------------------

To start the development server:

.. code-block:: bash

   python manage.py runserver

This will start the server at http://127.0.0.1:8000/. You can access the admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials you created.

Initial Configuration
-------------------

Before continuing with development, you might want to configure a few things:

1. Update the project name in ``django_project/settings.py``
2. Configure any environment-specific settings
3. Update the README.md file with your project's information

Next Steps
---------

Now that you have your project up and running, you can:

* Explore the admin interface
* Add your own apps and models
* Customize the templates and static files
* Learn about :doc:`customization` options for the template
* Read about :doc:`features` included in the template 