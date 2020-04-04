import json


def get_configuration(file):
    """Get the configuration from the setup.
    :returns: configuration

    """
    with open(file, "r") as configuration:
        return json.load(configuration)
