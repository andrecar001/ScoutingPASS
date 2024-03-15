from .match_scouting import *
from .pit_scouting import *
from .TBAInterface import *

def updateAllData(allDataPath, matchDataPath, pitDataPath):
    updateMatchScoutingFile(allDataPath,matchDataPath)
    updatePitScoutingFile(allDataPath,pitDataPath)