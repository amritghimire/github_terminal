LIST_PR = """
fragment pr on PullRequest {
    state
    headRefName
    title
    number
    changedFiles
    author {
        login
    }
    labels(first: 5) {
      nodes {
        name
      }
    }
}
  
  query(
  $query: String!,
  $limit: Int!
) {
  search(query: $query, type: ISSUE, last: $limit) {
    issueCount
    edges {
       node{
        ...pr
      }
    }
  }
}
"""
