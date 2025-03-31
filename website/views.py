from django.shortcuts import render


def home(request):
    """
    Home page view with responsive optimizations and enhanced context.
    """
    context = {}

    # Add PWA and mobile-specific metadata
    context["meta"] = {
        "title": "Django Project - Home",
        "description": "Welcome to the Django Project template",
        "viewport": "width=device-width, initial-scale=1, maximum-scale=5",
        "theme_color": "#0d6efd",  # Bootstrap primary color
    }

    return render(request, "website/home.html", context)


def about(request):
    """About page with app info."""
    return render(
        request,
        "website/about.html",
        {
            "meta": {
                "title": "About",
                "description": "Learn about our project",
            }
        },
    )


def contact(request):
    """Contact page."""
    return render(
        request,
        "website/contact.html",
        {
            "meta": {
                "title": "Contact Us",
                "description": "Get in touch with our team",
            }
        },
    )


def terms(request):
    """Terms page."""
    return render(
        request,
        "website/terms.html",
        {
            "meta": {
                "title": "Terms of Service",
                "description": "Our terms and conditions",
            }
        },
    )


def privacy(request):
    """Privacy policy."""
    return render(
        request,
        "website/privacy.html",
        {
            "meta": {
                "title": "Privacy Policy",
                "description": "How we protect your data",
            }
        },
    )


def faq(request):
    """FAQ page with mobile-friendly layout."""
    return render(
        request,
        "website/faq.html",
        {
            "meta": {
                "title": "Frequently Asked Questions",
                "description": "Get answers about Notes App",
                "mobile_app": True,
            }
        },
    )
