class Logger:
    """Class to log the message"""
    def __init__(self, verbose, quiet):
        self.verbose = verbose
        self.quiet = quiet

    def debug(self, message):
        """Print a debug message if verbose option is specified."""
        if self.verbose:
            print(message)

    def error(self, message):
        """Print a error message if quiet flag is not specified"""
        if not self.quiet:
            print(message)

    def info(self, message):
        """Print a message irrespective of the flags."""
        print(message)
