from gql import gql, Client

from gql.transport.requests import RequestsHTTPTransport
from ..configuration import Configuration
import urllib3
urllib3.disable_warnings()


class GQLClient():
    """Client to execute the GQL query from the api endpoint."""
    def __init__(self, args):
        """Initialize the GQL client with the authorization token and url.

        :args: Arguments from command line

        """
        self._configuration = Configuration(args)
        self._url = self._configuration.get_url()
        self._token = self._configuration.get_token()
        self.init_client()

    def init_client(self):
        """Initialize the client and transport structure
        """
        self._transport = RequestsHTTPTransport(url=self._url,
                                                use_json=True,
                                                headers={
                                                    "Content-type":
                                                    "application/json",
                                                    "Authorization":
                                                    "bearer " +
                                                    str(self._token).strip()
                                                },
                                                verify=False)
        self._client = Client(retries=3,
                              transport=self._transport,
                              fetch_schema_from_transport=False)

    def execute(self, query, params):
        """Execute the query

        :query: query to execute
        :params: Parameter for variable
        :returns: result

        """
        query_to_execute = gql(query)
        return self._client.execute(query_to_execute, variable_values=params)
