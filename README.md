# Django Project Template

A Django template repository with a custom user model that uses email-based authentication instead of username. This template provides a solid foundation for new Django projects.

## Using This Template

This is a GitHub template repository, which means you can generate a new repository with the same directory structure and files without forking it or including the commit history.

### Option 1: Use GitHub's "Use this template" feature
1. Click the green "Use this template" button at the top of the repository page
2. Choose "Create a new repository"
3. Enter your repository name and other details
4. Click "Create repository from template"

### Option 2: Clone and reinitialize
1. Clone the repository:
   ```
   git clone https://github.com/dehongi/django_project.git your-project-name
   cd your-project-name
   ```
2. Remove the existing git history and start fresh:
   ```
   rm -rf .git
   git init
   git add .
   git commit -m "Initial commit from template"
   ```

## Features

- Custom user model with email-based authentication
- User registration and authentication
- Password reset functionality
- User profiles with customizable fields
- Basic website structure with standard pages (home, about, contact, etc.)
- Bootstrap 5 integration with responsive design
- Clean organization of static files (CSS, JS, images)

## Setup Instructions

1. After creating your repository from the template, clone it to your local machine:
   ```
   git clone https://github.com/yourusername/your-project-name.git
   cd your-project-name
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

- Update `django_project/settings.py` with your project-specific settings:
  - Change the project name and other metadata
  - Configure database settings for your environment
  - Add or remove installed apps
  
- Modify templates in the `templates/` directory to match your design needs:
  - `templates/base.html` contains the main layout
  - App-specific templates are in their respective directories

- Extend the static files:
  - CSS files in `website/static/css/`
  - JavaScript in `website/static/js/`
  - Images in `website/static/img/`

- Extend the CustomUser model in `accounts/models.py` if you need additional fields

## Security Notes

- Before deploying to production, change the SECRET_KEY in settings.py (preferably use environment variables)
- Set DEBUG to False in production
- Configure proper email settings for password reset functionality
- Review and update the ALLOWED_HOSTS setting
- Consider using environment variables for sensitive configuration

## License

This project is licensed under the MIT License - see the LICENSE file for details.
