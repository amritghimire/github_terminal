import subprocess

GET_REPOSITORY = "git config --get remote.origin.url "\
    "| cut -d':' -f2- | cut -d'.' -f1"


def process_output(command):
    """Process output of the shell command and returns it.

    :command: Command to execute
    :returns: Output of the command.

    """
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    return str(proc.read().decode("utf-8")).strip()
