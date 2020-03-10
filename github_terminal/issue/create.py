from ..logger import Logger
from ..entry import Entry


def create_issue(args):
    """Create a new issue from the given parameter."""
    logger = Logger(args.verbose, args.quiet)
    entry = Entry(args)
    title = entry.ask("Title of the issue", argument="title")
    logger.debug("Creating issue with title {title}".format(title=title))
