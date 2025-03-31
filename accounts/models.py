from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
import re


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


class CustomUser(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.
    Uses email for authentication instead of username.
    Allows for easy addition of custom fields in the future.
    """

    # Required fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Additional fields
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )
    email = models.EmailField(unique=True, db_index=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    username = None  # Remove username since email is used instead

    slug = models.SlugField(max_length=50, unique=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

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
