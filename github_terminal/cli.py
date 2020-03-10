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
    args = parser.parse_args()
    category_specific_action = handle_category_action(args.category)
    category_specific_action(args.action, args)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
