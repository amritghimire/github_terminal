import json
from ..entry import Entry
from ..logger import Logger


def new_configuration(file, args):
    """Generates a new configuration and save it to the file.

    :file: File to store the config
    :returns: configuration

    """
    entry = Entry(args)
    logger = Logger(args.verbose, args.quiet)
    logger.info("Create personal access token at "
                "https://github.com/settings/tokens/new")
    configuration = {}
    configuration['token'] = entry.ask('Enter the github personal token ',
                                       default='',
                                       argument='token')
    configuration['username'] = entry.ask('Enter the github username ',
                                          default='',
                                          argument='username')
    with open(file, "w") as config:
        json.dump(configuration, config, sort_keys=True, indent=4)
    return configuration
