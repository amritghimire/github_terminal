"""Actions for issue category."""
from .list import list_pr


def get_action(action):
    """Get action according to the action."""
    return {
        'list': list_pr
    }.get(action, list_pr)


def pr(args):
    """Perform action according to the args"""
    action = args.action
    action = get_action(action)
    action(args)
