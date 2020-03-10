"""Actions for issue category."""
from .create import create_issue


def get_action(action):
    """Get action according to the action."""
    return {'create': create_issue}.get(action, create_issue)


def issue(action, args):
    """Perform action according to the args"""
    action = get_action(action)
    action(args)
