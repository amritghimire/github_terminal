LIST_ISSUES = """
query (
  $owner: String!,
  $repo: String!,
  $limit: Int!,
  $filters: IssueFilters) {
  repository(owner: $owner, name: $repo) {
    issues(last: $limit, filterBy: $filters) {
      edges {
        node {
          title
          number
          labels(first: 5) {
            nodes {
              name
            }
          }
        }
      }
    }
  }
}
"""
