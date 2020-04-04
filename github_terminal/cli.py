"""Console script for github_terminal."""
import argparse
import sys

from .github_terminal import handle_category_action


def main():
    """Console script for github_terminal."""
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v",
                       "--verbose",
                       action="store_true",
                       help="Show verbose information")
    group.add_argument("-q",
                       "--quiet",
                       action="store_true",
                       help="Display less information")
    parser.add_argument(
        'category',
        help='Use the task you want to create like issue, pr, repo ',
        choices=["issue", "pr", "repo"])
    parser.add_argument(
        'action',
        help='Use the action to perform in the category.',
        choices=["create", "list", "edit", "delete", "close", "status"])
    parser.add_argument("-t",
                        "--title",
                        help="Title of issue or PR or name of repository")
    parser.add_argument("-d",
                        "--description",
                        help="Description of issue or PR or repo.")
    parser.add_argument("-c", "--config", help="Configuration file to use.")
    parser.add_argument("-T",
                        "--token",
                        help="Personal access token for github.")
    parser.add_argument("-u", "--username", help="Username of the user")
    parser.add_argument("-a",
                        "--assignee",
                        help="Filter by assignee or set assignee")
    parser.add_argument("-b",
                        "--base",
                        help="Filter by base branch the pull request are being merged to (ONLY FOR PR AND REPO)")
    parser.add_argument("-A", "--author", help="Filter by or set author")
    parser.add_argument("-l",
                        "--label",
                        help="Filter or set label separated by comma")
    parser.add_argument("-L", "--limit", help="Maximum number to fetch")
    parser.add_argument("-s", "--state", help="Filter by state")
    parser.add_argument(
        "-S",
        "--since",
        help="List issues that have been updated at or after the given date."
        " (You can also use value like 2 weeks ago)")
    parser.add_argument("-r",
                        "--repo",
                        help="Repository to perform action on.")
    args = parser.parse_args()
    category_specific_action = handle_category_action(args)
    category_specific_action(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
