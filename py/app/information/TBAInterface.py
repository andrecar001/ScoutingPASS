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
    """-------------------------------------DISTRICTAPI-------------------------------------"""
    def getDistrictEvents(district_key):
        try:
            return district_api_instance.get_district_events(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling DistrictApi->get_event_matches: %s\n" % e)
    def getDistrictEventKeys(district_key):
        try:
            return district_api_instance.get_district_events_keys(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling DistrictApi->get_event_matches: %s\n" % e)
    def getDistrictEventsSimple(district_key):
        try:
            return district_api_instance.get_district_events_simple(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling DistrictApi->get_event_matches: %s\n" % e)
    def getDistrictRankings(district_key):
        try:
            return district_api_instance.get_district_rankings(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling DistrictApi->get_event_matches: %s\n" % e)
    def getDistrictTeams(district_key):
        try:
            return district_api_instance.get_district_teams(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling DistrictApi->get_event_matches: %s\n" % e)
    def getDistrictTeamsKeys(district_key):
        try:
            return district_api_instance.get_district_teams_keys(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling DistrictApi->get_event_matches: %s\n" % e)    
    def getDistrictTeamsSimples(district_key):
        try:
            return district_api_instance.get_district_teams_simple(district_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling DistrictApi->get_event_matches: %s\n" % e)
    def getDistrictsByYear(year):
        try:
            return district_api_instance.get_districts_by_year(year, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling DistrictApi->get_event_matches: %s\n" % e)


    """-------------------------------------EVENTAPI-------------------------------------"""
    def getEvent(event_key):
        try:
            return event_api_instance.get_event(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventAlliances(event_key):
        try:
            return event_api_instance.get_event_alliances(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventAwards(event_key):
        try:
            return event_api_instance.get_event_awards(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventDistrictPoints(event_key):
        try:
            return event_api_instance.get_event_district_points(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventInsights(event_key):
        try:
            return event_api_instance.get_event_insights(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventMatcheTimeseries(event_key):
        try:
            return event_api_instance.get_event_match_timeseries(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventMatches(event_key):
        try:
            return event_api_instance.get_event_matches(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventMatchesKeys(event_key):
        try:
            return event_api_instance.get_event_matches_keys(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventMatchesSimple(event_key):
        try:
            return event_api_instance.get_event_matches_simple(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventOPRs(event_key):
        try:
            return event_api_instance.get_event_op_rs(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventPredictions(event_key):
        try:
            return event_api_instance.get_event_predictions(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventRankings(event_key):
        try:
            return event_api_instance.get_event_rankings(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventSimple(event_key):
        try:
            return event_api_instance.get_event_simple(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventTeams(event_key):
        try:
            return event_api_instance.get_event_teams(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventTeamsKeys(event_key):
        try:
            return event_api_instance.get_event_teams_keys(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventTeamsNumbers(event_key):
        team_keys = getEventTeamsKeys(event_key)
        team_numbers = []
        for team in team_keys:
            team_numbers.append(team[3:])
        return team_numbers
    def getEventTeamsSimple(event_key):
        try:
            return event_api_instance.get_event_teams_simple(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventTeamsStatuses(event_key):
        try:
            return event_api_instance.get_event_teams_statuses(event_key, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventsByYear(year):
        try:
            return event_api_instance.get_events_by_year(year, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventsByYearKeys(year):
        try:
            return event_api_instance.get_events_by_year_keys(year, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    def getEventsByYearSimple(year):
        try:
            return event_api_instance.get_events_by_year_simple(year, if_modified_since=if_modified_since)
        except ApiException as e:
            print("Exception when calling EventApi->get_event_op_rs: %s\n" % e)
    
    #LISTAPI
            

    """-------------------------------------MATCHAPI-------------------------------------"""
    def getMatch(event_key):
        try:
            return match_api_instance.get_match(event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    def getMatchSimple(match_key):
        try:
            return match_api_instance.get_match_simple(match_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    def getMatchTimeseries(match_key):
        try:
            return match_api_instance.get_match_timeseries(match_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    def getMatchZebra(match_key):
        try:
            return match_api_instance.get_match_zebra(match_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling MatchApi->get_event_matches: %s\n" % e)
    
    """-------------------------------------TEAMAPI-------------------------------------"""
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
    def getTeamAwardsByYear(event_key,year):
        try:
            return team_api_instance.get_team_awards_by_year(event_key, year, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamDistricts(team_key):
        try:
            return team_api_instance.get_team_districts(team_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamEventAwards(team_key, event_key):
        try:
            return team_api_instance.get_team_event_awards(team_key, event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamEventMatches(team_key, event_key):
        try:
            return team_api_instance.get_team_event_matches(team_key, event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamEventMatchesKeys(team_key, event_key):
        try:
            return team_api_instance.get_team_event_matches_keys(team_key, event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamEventMatchesSimple(team_key, event_key):
        try:
            return team_api_instance.get_team_event_matches_simple(team_key, event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamEventStatus(team_key, event_key):
        try:
            return team_api_instance.get_team_event_status(team_key, event_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamEvents(team_key):
        try:
            return team_api_instance.get_(team_key, if_modified_since=if_modified_since)    
        except ApiException as e:
            print("Exception when calling TeamApi->get_event_matches: %s\n" % e)
    def getTeamEventsByYear(team_key, year):
        try:
            return team_api_instance.get_(team_key, year, if_modified_since=if_modified_since)    
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

    eventOprs = getEventOPRs(EVENT_KEY).oprs
    eventDprs = getEventOPRs(EVENT_KEY).dprs
    eventCCWMs = getEventOPRs(EVENT_KEY).ccwms
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
# teams = getEventInfo()
# print(getEventTeamsSimple(EVENT_KEY))

# addOPRs(teams)
# pprint(teams)

matches = getTeamEventMatches(TEAM,EVENT_KEY)
# print(matches)
# addOPRs(teams)
matchNums = [8,14,25,36,47,53,60,70,80]
matchIdx = 0

def getOurMatches():
    for match in matches:
        red_teams = ""
        blue_teams = ""
        for team in match.alliances.blue.team_keys:
            blue_teams += (team[3:] + "%")
        for team in match.alliances.red.team_keys:
            red_teams += (team[3:] + "%")
        print(f"{matchNums[matchIdx]}%Blue%{blue_teams}")
        print(f"{matchNums[matchIdx]}%Red%{red_teams}")
        matchIdx += 1
    # print(match.alliances)

# for team in teams.values():
#     num = team["team_number"]
#     nick = team["nickname"]
#     loc = team["location"]
#     # print(f"{num}%{nick}%{loc}%{team['OPR']}%{team['DPR']}")
#     # print(team)