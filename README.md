# Django Project Template

A Django template project with a custom user model that uses email-based authentication instead of username. This template provides a solid foundation for new Django projects.

## Features

- Custom user model with email-based authentication
- User registration and authentication
- Password reset functionality
- User profiles with customizable fields
- Basic website structure with standard pages (home, about, contact, etc.)
- Bootstrap-ready templates (requires adding Bootstrap)

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/dehongi/django_project.git
   cd django_project
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the site at http://127.0.0.1:8000/

## Customization

This template is designed to be customized for your specific project needs:

- Update `django_project/settings.py` with your project-specific settings
- Modify templates in the `templates/` directory to match your design
- Add CSS/JS files to the static directories
- Extend the CustomUser model in `accounts/models.py` if you need additional fields

## Security Notes

- Before deploying to production, change the SECRET_KEY in settings.py
- Set DEBUG to False in production
- Configure proper email settings for password reset functionality
- Review and update the ALLOWED_HOSTS setting

## License

This project is licensed under the MIT License - see the LICENSE file for details.
