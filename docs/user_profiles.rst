User Profiles
============

The Django Project Template includes a comprehensive user profile system that extends the custom user model with additional functionality.

Profile Model
------------

The profile functionality is built into the ``CustomUser`` model in ``accounts/models.py``. This integrated approach avoids the need for a separate profile model and simplifies the codebase.

Key profile fields include:

* ``first_name`` and ``last_name``: Required fields for user's name
* ``email``: Used for authentication and communication
* ``bio``: Text field for user's biography or description
* ``profile_picture``: Image field for user's profile picture
* ``slug``: URL-friendly identifier for user profiles

Slug Generation
-------------

The template automatically generates a slug for each user based on their name or email. This is handled in the ``save`` method of the ``CustomUser`` model:

.. code-block:: python

    def save(self, *args, **kwargs):
        if not self.slug:
            # Get the username portion of the email (before @)
            email_name = self.email.split("@")[0]

            # Remove special characters and replace with hyphens
            base_slug = re.sub(r"[^\w\s-]", "-", email_name.lower())
            base_slug = re.sub(r"[-\s]+", "-", base_slug).strip("-")

            # If user has a name, try to incorporate it into the slug
            if self.first_name and self.last_name:
                name_slug = slugify(f"{self.first_name}-{self.last_name}")
                # Use combination of name and email if possible
                if len(name_slug) > 5:  # Only use name if it creates a reasonable slug
                    base_slug = name_slug

            # Ensure uniqueness by adding a suffix if needed
            slug = base_slug
            counter = 1

            while CustomUser.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

This approach ensures that:

1. Every user has a unique, URL-friendly slug
2. The slug is based on the user's name if available, otherwise on their email
3. Special characters are properly handled
4. Potential duplicate slugs are resolved by adding a numeric suffix

Profile Views
-----------

The template provides several views for working with user profiles:

1. ``ProfileView``: Shows the logged-in user's profile
2. ``PublicProfileView``: Shows a public view of a user's profile (accessible to anyone)
3. ``ProfileUpdateView``: Allows users to edit their profile information

These views are defined in ``accounts/views.py`` and are class-based views that extend Django's generic views.

Profile View
^^^^^^^^^^

The ``ProfileView`` shows the logged-in user's profile and is accessible only to authenticated users:

.. code-block:: python

    class ProfileView(LoginRequiredMixin, DetailView):
        model = CustomUser
        template_name = "accounts/profile.html"
        context_object_name = "user"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["meta"] = {
                "title": "Profile",
                "description": "View your profile information",
                "viewport": "width=device-width, initial-scale=1.0",
            }
            return context

        def get_object(self):
            return self.request.user

Public Profile View
^^^^^^^^^^^^^^^^

The ``PublicProfileView`` shows a public view of a user's profile and is accessible to anyone:

.. code-block:: python

    class PublicProfileView(DetailView):
        model = CustomUser
        template_name = "accounts/public_profile.html"
        context_object_name = "profile_user"
        slug_field = "slug"
        slug_url_kwarg = "slug"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["meta"] = {
                "title": f"{self.object.get_full_name()}'s Profile",
                "description": f"View {self.object.get_full_name()}'s public profile",
                "viewport": "width=device-width, initial-scale=1.0",
            }
            return context

Profile Update View
^^^^^^^^^^^^^^^^

The ``ProfileUpdateView`` allows users to edit their profile information:

.. code-block:: python

    class ProfileUpdateView(LoginRequiredMixin, UpdateView):
        model = CustomUser
        form_class = ProfileUpdateForm
        template_name = "accounts/profile_update.html"
        success_url = reverse_lazy("accounts:profile")

        def get_object(self):
            return self.request.user

        def form_valid(self, form):
            messages.success(self.request, "Your profile has been updated!")
            return super().form_valid(form)

Profile URLs
----------

The profile URLs are configured in ``accounts/urls.py``:

.. code-block:: python

    # Profile
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/edit/", views.ProfileUpdateView.as_view(), name="profile_edit"),
    path("profile/<str:slug>/", views.PublicProfileView.as_view(), name="public_profile"),

These URLs allow:

* ``/accounts/profile/``: Access to the user's own profile
* ``/accounts/profile/edit/``: Form to edit the user's profile
* ``/accounts/profile/<slug>/``: Public view of a user's profile

Profile Templates
--------------

The template includes three main templates for user profiles:

1. ``templates/accounts/profile.html``: Template for viewing own profile
2. ``templates/accounts/public_profile.html``: Template for viewing someone else's profile
3. ``templates/accounts/profile_update.html``: Form for updating profile

These templates use Bootstrap for styling and are fully responsive.

Profile Form
----------

The profile update form is defined in ``accounts/forms.py``:

.. code-block:: python

    class ProfileUpdateForm(forms.ModelForm):
        class Meta:
            model = CustomUser
            fields = ["first_name", "last_name", "email", "bio", "profile_picture"]
            widgets = {
                "bio": forms.Textarea(attrs={"rows": 4}),
            }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Add Bootstrap classes
            for field in self.fields:
                self.fields[field].widget.attrs.update({"class": "form-control"})

        def clean_email(self):
            email = self.cleaned_data.get("email")
            user_id = self.instance.id
            
            # Check if email is already taken by another user
            if CustomUser.objects.filter(email=email).exclude(id=user_id).exists():
                raise forms.ValidationError("This email is already in use.")
            
            return email

This form:

1. Allows users to update their basic information and profile picture
2. Includes validation to prevent email duplication
3. Includes Bootstrap styling
4. Customizes the bio field to use a textarea

Profile Pictures
--------------

The template handles profile pictures using Django's ``ImageField``. Profile pictures are stored in the ``media/profile_pictures/`` directory.

The templates include fallback display for users without profile pictures, showing their initials in a colored circle.

Customizing Profiles
-----------------

To customize the profile system:

1. Add or modify fields in the ``CustomUser`` model in ``accounts/models.py``
2. Update the profile form in ``accounts/forms.py`` to include the new fields
3. Modify the profile templates to display the new fields
4. Add validation or custom methods as needed

For example, to add a "location" field:

1. Add the field to the model:

   .. code-block:: python

       class CustomUser(AbstractUser):
           # Existing fields...
           location = models.CharField(max_length=100, blank=True, null=True)
           # ...

2. Add the field to the form:

   .. code-block:: python

       class ProfileUpdateForm(forms.ModelForm):
           class Meta:
               model = CustomUser
               fields = ["first_name", "last_name", "email", "bio", "location", "profile_picture"]
               # ...

3. Update the templates to display the field
4. Run migrations to apply the database changes

Remember to run migrations whenever you modify the user model:

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate 