import os.path


def check_configuration(file):
    """Check if the configuration file exists in the system."""
    return os.path.isfile(file)
