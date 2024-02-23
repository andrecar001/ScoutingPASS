from __future__ import print_function

import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.thebluealliance.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = tbaapiv3client.Configuration(
    host = "https://www.thebluealliance.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration = tbaapiv3client.Configuration(
    host = "https://www.thebluealliance.com/api/v3",
    api_key = {
        'X-TBA-Auth-Key': '2hKZge8yV9nkehbD8bOXGBrHNgUzD9eSNHPZnaIWIQFHCO6DhFKkQLFVFaoyja8k'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'


# Enter a context with an instance of the API client

### TEAMS ###
def getTeamsSimple(event_key):
    with tbaapiv3client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = tbaapiv3client.TeamApi(api_client)
        #event_key = '2024mnkk' # str | TBA Event Key, eg `2016nytr`
        if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)
        
        try:
            api_response = api_instance.get_event_teams_simple(event_key, if_modified_since=if_modified_since)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_teams_keys: %s\n" % e)


### MATCHES ###
def getEventMatches(event_key):
    with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
        api_instance = tbaapiv3client.MatchApi(api_client)
        #event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
        if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

        try:
            api_response = api_instance.get_event_matches_keys(event_key, if_modified_since=if_modified_since)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)

getEventMatches('2023ndgf')