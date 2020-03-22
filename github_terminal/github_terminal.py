"""Main module."""
from .issue import issue


def handle_category_action(args):
    """Handle the category specific action."""
    category = args.category
    return {'issue': issue}.get(category, issue)
