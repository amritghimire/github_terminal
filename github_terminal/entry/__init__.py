"""A class to handle the entry"""


class Entry:
    """Handle the entry from user."""
    def __init__(self, args):
        """Initialize argument."""
        self.quiet = args.quiet
        self.args = vars(args)

    def ask(self, message, default=None, transform=str, argument=None):
        """Ask the user for the response."""
        if self.quiet:
            return transform(default)
        if argument and self.args.get(argument):
            return transform(self.args.get(argument))
        response = transform(input(f'{message} [{default}]'))
        return response if response else transform(default)
