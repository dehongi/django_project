Features
========

This template includes several pre-configured features to help you get started quickly. This page describes these features in detail.

Custom User Model
----------------

The template uses a custom user model that replaces Django's default username-based authentication with email-based authentication. This is implemented in the ``accounts`` app.

Key characteristics:

* Email is used as the username field for authentication
* Username field is removed
* First name and last name are required fields
* Custom user manager for creating users and superusers
* Profile picture field using Django's ImageField
* Bio field for user information
* Custom slug field for user profiles

Benefits of email-based authentication:

* Users don't need to remember another username
* Email addresses are unique
* Simplifies the user registration process
* More flexibility for extending the user model in the future

Authentication System
-------------------

The template includes a complete authentication system with the following features:

* User registration with email verification
* Login and logout functionality
* Password reset with email confirmation
* Password change for authenticated users
* Custom forms with Bootstrap styling
* Protection against common security threats (CSRF, brute force, etc.)

All authentication templates are customized with Bootstrap and ready for use.

User Profiles
------------

The template includes a user profile system with:

* Public profile pages accessible via user slug
* Profile editing with form validation
* Profile picture upload and display
* User bio and personal information

Bootstrap 5 Integration
---------------------

The template is fully integrated with Bootstrap 5, providing:

* Responsive layout that works on all devices
* Modern, clean UI components
* Navigation system with dropdown menus
* Card layouts for content presentation
* Form styling with validation
* Alert messages
* Icons via Bootstrap Icons

Page Structure
-------------

The template includes the following pages:

* Home page with hero section and features
* About page with template information
* Contact page template
* Terms and Privacy policy templates
* User authentication pages (login, register, password reset, etc.)
* User profile pages

Static Files Organization
-----------------------

The static files are organized into a clean structure:

* CSS files in ``website/static/css/`` with a main ``styles.css`` file
* JavaScript in ``website/static/js/`` with a main ``script.js`` file
* Images in ``website/static/img/`` with favicon
* Web app manifest file for progressive web app support

Message Framework
---------------

The template uses Django's message framework for displaying notifications to users:

* Success messages after successful operations
* Error messages when something goes wrong
* Warning messages for important information
* Info messages for general notifications

Messages are styled with Bootstrap alert classes and automatically displayed in the base template.

Responsive Design
---------------

The template is fully responsive and works well on:

* Desktop computers
* Tablets
* Mobile phones

This is achieved through:

* Bootstrap's responsive grid system
* Mobile-first approach
* Custom CSS media queries
* Responsive navigation

Security Features
---------------

The template includes several security features:

* CSRF protection on all forms
* Password validation with Django's built-in validators
* Protection against common web vulnerabilities
* Secure password reset process
* Proper handling of user authentication

Extendability
------------

The template is designed to be easily extended:

* Clear separation of apps (accounts, website)
* Modular templates with inheritance
* Block tags for extending specific parts of templates
* Well-structured static files
* Well-documented code 