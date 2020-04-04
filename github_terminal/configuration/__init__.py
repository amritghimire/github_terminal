from json.decoder import JSONDecodeError
from .check import check_configuration
from os.path import expanduser
from .get import get_configuration
from .new import new_configuration

from ..logger import Logger
from ..lang import errors
from ..utils.shell import process_output, GET_REPOSITORY


class Configuration():
    """Configuration for the github terminal project."""
    def __init__(
        self,
        args,
        url="https://api.github.com/graphql",
        file="~/.github_terminal.config",
    ):
        """Initialize the configuration from the project.

        :url: URL for the github api.

        """
        self._url = url
        self._file = expanduser(file)
        self._args = args
        self._repo = None
        self._logger = Logger(self._args.verbose, self._args.quiet)
        if args.config:
            self._file = expanduser(args.config)
        self.make_sure_config_file_exists()

    def make_sure_config_file_exists(self):
        """Check if the config file exists and create if doesnot exists.
        """
        try:
            self._configuration = get_configuration(
                self._file) if check_configuration(
                    self._file) else new_configuration(self._file, self._args)
        except (JSONDecodeError):
            self._logger.error(errors.INVALID_CONFIGURATION, exit=True)

    def get_repository(self):
        """Get the current repository to run the code.
        :returns: Repository name

        """
        if self._args.repo:
            return self._args.repo

        if self._repo:
            return self._repo
        self._repo = process_output(GET_REPOSITORY)
        if not self._repo:
            self._logger.error(
                "Cannot get repository information from the path."
                " Please use --repo or go to the path with git index",
                exit=True)
        return self._repo

    def get_url(self):
        """Get the url for Graphql connection
        :returns: URL

        """
        return self._url

    def get_token(self):
        """Get token from the configuration
        :returns: token

        """
        return self._configuration['token'] or ''
