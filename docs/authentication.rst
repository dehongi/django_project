Authentication
==============

The Django Project Template comes with a complete authentication system based on Django's built-in authentication framework, but with a custom user model that uses email instead of username.

Custom User Model
----------------

The custom user model is defined in ``accounts/models.py`` and extends Django's ``AbstractUser`` model:

.. code-block:: python

    class CustomUser(AbstractUser):
        # Remove username field
        username = None
        
        # Required fields
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        
        # Email for authentication
        email = models.EmailField(unique=True, db_index=True)
        USERNAME_FIELD = "email"
        REQUIRED_FIELDS = ["first_name", "last_name"]
        
        # Additional fields
        bio = models.TextField(blank=True, null=True)
        profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
        slug = models.SlugField(max_length=50, unique=True, blank=True)
        
        objects = CustomUserManager()
        
        # ...

This model configuration:

* Removes the username field
* Sets email as the USERNAME_FIELD for authentication
* Makes first_name and last_name required fields
* Adds additional fields like bio, profile_picture, and slug

Custom User Manager
-----------------

The custom user manager in ``accounts/models.py`` provides methods for creating users and superusers:

.. code-block:: python

    class CustomUserManager(BaseUserManager):
        """
        Custom user manager for email-based authentication instead of username.
        """
        
        def create_user(self, email, password=None, **extra_fields):
            if not email:
                raise ValueError("The Email field must be set")
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        
        def create_superuser(self, email, password=None, **extra_fields):
            extra_fields.setdefault("is_staff", True)
            extra_fields.setdefault("is_superuser", True)
            extra_fields.setdefault("is_active", True)
            
            if extra_fields.get("is_staff") is not True:
                raise ValueError("Superuser must have is_staff=True.")
            if extra_fields.get("is_superuser") is not True:
                raise ValueError("Superuser must have is_superuser=True.")
            
            return self.create_user(email, password, **extra_fields)

Authentication Forms
------------------

The template includes custom authentication forms in ``accounts/forms.py``:

1. ``CustomUserCreationForm``: For user registration
2. ``CustomAuthenticationForm``: For login
3. ``CustomPasswordResetForm``: For initiating password reset
4. ``CustomSetPasswordForm``: For setting a new password during reset
5. ``CustomPasswordChangeForm``: For changing password when logged in
6. ``ProfileUpdateForm``: For updating user profile information

These forms are styled with Bootstrap and include client-side validation.

Authentication Views
-----------------

The authentication views are defined in ``accounts/views.py`` and include:

1. ``SignUpView``: For user registration
2. ``CustomLoginView``: For user login
3. ``CustomLogoutView``: For user logout
4. ``CustomPasswordResetView``: For initiating password reset
5. ``CustomPasswordResetDoneView``: Confirmation after password reset request
6. ``CustomPasswordResetConfirmView``: For setting a new password
7. ``CustomPasswordResetCompleteView``: Confirmation after password reset
8. ``CustomPasswordChangeView``: For changing password
9. ``CustomPasswordChangeDoneView``: Confirmation after password change

URL Configuration
---------------

The authentication URLs are configured in ``accounts/urls.py``:

.. code-block:: python

    urlpatterns = [
        path("signup/", views.SignUpView.as_view(), name="signup"),
        path("login/", views.CustomLoginView.as_view(), name="login"),
        path("logout/", views.CustomLogoutView.as_view(), name="logout"),
        # Password reset
        path("password-reset/", views.CustomPasswordResetView.as_view(), name="password_reset"),
        path("password-reset/done/", views.CustomPasswordResetDoneView.as_view(), name="password_reset_done"),
        path("password-reset/confirm/<uidb64>/<token>/", views.CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
        path("password-reset/complete/", views.CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),
        # Password change
        path("password-change/", views.CustomPasswordChangeView.as_view(), name="password_change"),
        path("password-change/done/", views.CustomPasswordChangeDoneView.as_view(), name="password_change_done"),
        # Profile
        path("profile/", views.ProfileView.as_view(), name="profile"),
        path("profile/edit/", views.ProfileUpdateView.as_view(), name="profile_edit"),
        path("profile/<str:slug>/", views.PublicProfileView.as_view(), name="public_profile"),
    ]

Authentication Templates
---------------------

The authentication templates are located in ``templates/accounts/`` and include:

1. ``signup.html``: User registration form
2. ``login.html``: Login form
3. ``password_reset.html``: Form to request password reset
4. ``password_reset_done.html``: Confirmation after reset request
5. ``password_reset_confirm.html``: Form to set new password
6. ``password_reset_complete.html``: Confirmation after reset
7. ``password_change.html``: Form to change password
8. ``password_change_done.html``: Confirmation after change
9. ``password_reset_email.html``: Email template for reset link
10. ``password_reset_subject.txt``: Subject line for reset email

Email Configuration
----------------

For password reset functionality to work in production, configure the email settings in ``django_project/settings.py``:

.. code-block:: python

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.example.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your-email@example.com'
    EMAIL_HOST_PASSWORD = 'your-password'
    DEFAULT_FROM_EMAIL = 'Your Project <noreply@example.com>'

For development, the template uses the console backend that prints emails to the console:

.. code-block:: python

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Authentication Redirects
---------------------

The template configures authentication redirects in ``django_project/settings.py``:

.. code-block:: python

    LOGIN_REDIRECT_URL = "website:home"
    LOGOUT_REDIRECT_URL = "website:home"
    LOGIN_URL = "accounts:login"

These settings determine:

* Where users are redirected after login (the home page)
* Where users are redirected after logout (the home page)
* Where users are redirected if they try to access a protected page without being logged in (the login page)

Password Validation
-----------------

The template uses Django's built-in password validators:

.. code-block:: python

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

These validators ensure that:

* Passwords are not too similar to user attributes
* Passwords have a minimum length
* Passwords are not too common
* Passwords are not entirely numeric

Customizing Authentication
-----------------------

To customize the authentication system:

1. Modify the ``CustomUser`` model in ``accounts/models.py`` to add or change fields
2. Update the forms in ``accounts/forms.py`` to reflect model changes
3. Modify the templates in ``templates/accounts/`` to change the appearance
4. Update the views in ``accounts/views.py`` to change behavior
5. Configure email settings for production

Remember to run migrations if you change the user model:

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate 