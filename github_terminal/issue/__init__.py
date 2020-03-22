"""Actions for issue category."""
from .create import create_issue
from .list import list_issues


def get_action(action):
    """Get action according to the action."""
    return {
        'create': create_issue,
        'list': list_issues
    }.get(action, create_issue)


def issue(args):
    """Perform action according to the args"""
    action = args.action
    action = get_action(action)
    action(args)
