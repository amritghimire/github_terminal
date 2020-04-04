import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger:
    """Class to log the message"""
    def __init__(self, verbose, quiet):
        self.verbose = verbose
        self.quiet = quiet

    def debug(self, message):
        """Print a debug message if verbose option is specified."""
        if self.verbose:
            print(bcolors.OKBLUE, message, bcolors.ENDC)

    def error(self, message, exit=False):
        """Print a error message if quiet flag is not specified"""
        if not self.quiet:
            print(bcolors.FAIL, message, bcolors.ENDC)
        if exit:
            sys.exit(1)

    def info(self, message):
        """Print a message irrespective of the flags."""
        print(message)
