import moment

from ..logger import Logger, bcolors
from ..configuration import Configuration
from ..request.gql import GQLClient
from ..request.query.pr import LIST_PR


def append_to_query(logger, query, param, value):
    logger.debug("Only showing pull request with {param} {value}".format(param=param, value=value))
    return "{query} {param}:{value}".format(query=query, param=param, value=value)


def list_pr(args):
    """List the pull requests from given filters"""
    logger = Logger(args.verbose, args.quiet)
    configuration = Configuration(args)
    repo = configuration.get_repository()
    logger.debug("Listing the pull requests from github repository {repo}".format(repo=repo))
    limit = int(args.limit) if args.limit else 10
    logger.debug("Limiting the count to {limit}".format(limit=limit))
    query = "repo:{repo} type:pr".format(repo=repo)
    if args.assignee:
        query = append_to_query(logger, query, 'assignee', args.assignee)
    if args.author:
        query = append_to_query(logger, query, 'author', args.author)
    if args.label:
        labels = str(args.label).split(',')
        for label in labels:
            query = append_to_query(logger, query, 'label', label)
    if args.state:
        query = append_to_query(logger, query, 'state', args.state)
    if args.base:
        query = append_to_query(logger, query, 'base', args.base)
    if args.since:
        date = moment.date(args.since)
        if date:
            query = append_to_query(logger, query, 'created', '>{date}'.format(date=date.format('YYYY-MM-DD')))
    variables = {
        "limit": limit,
        "query": query
    }
    gql = GQLClient(args)
    logger.debug('Fetching api request.')
    prs = gql.execute(LIST_PR, variables)
    logger.info(' ')
    logger.info("Showing {limit} Pull requests  out of {total} for {repo}".format(limit=limit,
                                                                                  total=prs["search"][
                                                                                      "issueCount"], repo=repo))
    logger.info(' ')
    shown = False
    for pr_node in prs["search"]["edges"]:
        pr = pr_node['node']
        shown = True
        label = ', '.join([node['name'] for node in pr["labels"]["nodes"]])
        if label:
            label = '({})'.format(label)
        logger.info('{color}{number:5}{end} {title:83} {file:5} file changed.  {labels}'.format(
            color=bcolors.OKGREEN,
            number='#' + str(pr['number']),
            end=bcolors.ENDC,
            file=pr['changedFiles'],
            title=pr['title'][:80] + ('...' if len(pr['title']) > 80 else ''),
            labels=label))
    if not shown:
        logger.info('{color}No pull requests found{end}'.format(color=bcolors.WARNING,
                                                                end=bcolors.ENDC))
