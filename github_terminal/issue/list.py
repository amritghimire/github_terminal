import moment

from ..logger import Logger, bcolors
from ..configuration import Configuration
from ..request.gql import GQLClient
from ..request.query.issue import LIST_ISSUES


def list_issues(args):
    """Create a new issue from the given parameter."""
    logger = Logger(args.verbose, args.quiet)
    configuration = Configuration(args)
    repo = configuration.get_repository()
    logger.debug(
        "Listing the issues from github repository {repo}".format(repo=repo))
    owner, repository = repo.split('/')
    limit = args.limit if args.limit else 10
    logger.debug("Limiting the count to {limit}".format(limit=limit))
    filters = {}
    if args.assignee:
        filters["assignee"] = args.assignee
        logger.debug('Only showing issues assigned to {assignee}'.format(
            assignee=args.assignee))
    if args.author:
        filters["createdBy"] = args.author
        logger.debug('Only showing issues authored by {}'.format(args.author))
    if args.label:
        filters["labels"] = str(args.label).split(',')
        logger.debug("Limiting the issues with label {}".format(args.label))
    if args.state:
        filters["states"] = args.state
        logger.debug("Only showing {} issue".format(args.state))
    if args.since:
        date = moment.date(args.since)
        if date:
            filters["since"] = date.date.isoformat()
            logger.debug("Showing issues since {}".format(date))
    variables = {
        "owner": owner,
        "repo": repository,
        "limit": limit,
        "filters": filters
    }
    gql = GQLClient(args)
    logger.debug('Fetching api request.')
    issues = gql.execute(LIST_ISSUES, variables)
    logger.info(' ')
    logger.info("Showing issues for {}".format(repo))
    logger.info(' ')
    shown = False
    for issue_node in issues["repository"]["issues"]["edges"]:
        issue = issue_node['node']
        shown = True
        label = ', '.join([node['name'] for node in issue["labels"]["nodes"]])
        if label:
            label = '({})'.format(label)
            logger.info('{color}{number:5}{end} {title:60} {labels}'.format(
                color=bcolors.OKGREEN,
                number='#' + str(issue['number']),
                end=bcolors.ENDC,
                title=issue['title'],
                labels=label))
    if not shown:
        logger.info('{color}No issues found{end}'.format(color=bcolors.WARNING,
                                                         end=bcolors.ENDC))
