"""Main module."""
from .issue import issue
from .pr import pr


def handle_category_action(args):
    """Handle the category specific action."""
    category = args.category
    return {'issue': issue, 'pr': pr}.get(category, issue)
