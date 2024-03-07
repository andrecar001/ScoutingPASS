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
def getEventTeamsSimple(event_key):
    with tbaapiv3client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = tbaapiv3client.TeamApi(api_client)
        #event_key = '2024mnkk' # str | TBA Event Key, eg `2016nytr`
        if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)
        
        try:
            api_response = api_instance.get_event_teams_simple(event_key, if_modified_since=if_modified_since)
            return api_response
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_teams_keys: %s\n" % e)

### MATCHES ###
# def getEventMatches(event_key):
#     with tbaapiv3client.ApiClient(configuration) as api_client:
#     # Create an instance of the API class
#         api_instance = tbaapiv3client.MatchApi(api_client)
#         #event_key = 'event_key_example' # str | TBA Event Key, eg `2016nytr`
#         if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

#         try:
#             api_response = api_instance.get_event_matches_keys(event_key, if_modified_since=if_modified_since)
#             return api_response
#         except ApiException as e:
#             print("Exception when calling MatchApi->get_event_matches: %s\n" % e)

    # print(getTeamsSimple('2024mnkk'))
            
    with tbaapiv3client.ApiClient(configuration) as api_client:
        api_instance = tbaapiv3client.EventApi(api_client)
    # Create an instance of the API class


with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class

    # Define Variables/api instances
    if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)
    event_api_instance = tbaapiv3client.EventApi(api_client)
    team_api_instance = tbaapiv3client.TeamApi(api_client)
    match_api_instance = tbaapiv3client.MatchApi(api_client)
    district_api_instance = tbaapiv3client.DistrictApi(api_client)
    list_api_instance = tbaapiv3client.ListApi(api_client)

    ### API FUNCTIONS ###
    # EVENTS
    def getEventTeamsSimple(event_key):
        try:
            return team_api_instance.get_event_teams_simple(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)

    def getEventOPR(event_key):
        try:
            return event_api_instance.get_event_op_rs(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    # MATCHAPI
    def getEventMatches(event_key):
        try:
            return match_api_instance.get_event_matches(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    def getEventMatchesSimple(event_key):
        try:
            return match_api_instance.get_event_matches_simple(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    def getMatch(event_key):
        try:
            return match_api_instance.get_match(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    def getTeamEventMatches(event_key):
        try:
            return match_api_instance.get_team_event_matches(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    def getTeamMatchesSimple(event_key):
        try:
            return match_api_instance.get_team_event_matches_simple(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    def getTeamMatchesByYear(event_key):
        try:
            return match_api_instance.get_team_matches_by_year(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    def getTeamMatchesByYearKeys(event_key):
        try:
            return match_api_instance.get_team_matches_by_year_keys(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    def getTeamMatchesByYearSimple(event_key):
        try:
            return match_api_instance.get_team_matches_by_year_simple(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    # TEAMAPI
    def getDistrictRankings(district_key):
        try:
            return team_api_instance.get_district_rankings(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getDistrictTeams(district_key):
        try:
            return team_api_instance.get_district_teams(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getDistrictTeamsKeys(district_key):
        try:
            return team_api_instance.get_district_teams_keys(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getDistrictTeamsSimple(district_key):
        try:
            return team_api_instance.get_district_teams_simple(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getEventTeams(event_key):
        try:
            return team_api_instance.get_event_teams(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getEventTeamsKeys(event_key):
        try:
            return team_api_instance.get_event_teams_keys(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getEventTeamsSimple(event_key):
        try:
            return team_api_instance.get_event_teams_simple(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getEventTeamsStatuses(event_key):
        try:
            return team_api_instance.get_event_teams_statuses(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeam(team_key):
        try:
            return team_api_instance.get_team(team_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamAwards(event_key):
        try:
            return team_api_instance.get_team_awards(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamAwardsByYear(event_key):
        try:
            return team_api_instance.get_team_awards_by_year(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamDistricts(event_key):
        try:
            return team_api_instance.get_team_districts(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamEventAwards(event_key):
        try:
            return team_api_instance.get_team_event_awards(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamEventMatches(event_key):
        try:
            return team_api_instance.get_team_event_matches(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamEventMatchesKeys(event_key):
        try:
            return team_api_instance.get_team_event_matches_keys(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(team_key, event_key):
        try:
            return team_api_instance.get_(team_key, event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def get(event_key):
        try:
            return team_api_instance.get_(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)


### MAIN CODE ###
def getEventInfo():

    teams = getEventTeamsSimple(EVENT_KEY)
    team_vals = {}
    #Base team info
    for team in teams:
        # print(team)
        temp_obj = {}
        #temp_obj["key"] = team.key
        temp_obj["team_number"] = team.team_number
        temp_obj["nickname"] = team.nickname
        temp_obj["location"] = (team.city + ", " + team.state_prov)
        team_vals[team.key] = temp_obj

 
    return team_vals

def addOPRs(team_vals):
    #OPRs, DPRs, CCWMs

    eventOprs = getEventOPR(EVENT_KEY).oprs
    eventDprs = getEventOPR(EVENT_KEY).dprs
    eventCCWMs = getEventOPR(EVENT_KEY).ccwms
    if eventOprs != None:
        for opr in eventOprs:
            team_vals[str(opr)]["OPR"] = eventOprs[opr]
    if eventDprs != None:
        for dpr in eventDprs:
            if dpr != None: team_vals[str(dpr)]["DPR"] = eventDprs[dpr]
    if eventCCWMs != None:
        for ccwm in eventCCWMs:
            if ccwm != None: team_vals[str(ccwm)]["CCWM"] = eventCCWMs[ccwm]
# EVENT ="2023ndgf"
            

TEAM = "frc2508"
EVENT_KEY = "2024ndgf"
teams = getEventInfo()
pprint(getEventMatches(EVENT_KEY))

# addOPRs(teams)


# for team in teams.values():
#     num = team["team_number"]
#     nick = team["nickname"]
#     loc = team["location"]
#     print(f"{num}\t{nick}\t{loc}")
#     # print(team)
