"""Main module."""
from .issue import issue


def handle_category_action(category):
    """Handle the category specific action."""
    return {'issue': issue}.get(category, issue)
