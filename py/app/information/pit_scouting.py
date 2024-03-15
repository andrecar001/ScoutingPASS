class DotDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
def getAllPitInfo(filePath):
#Create Dictionary
    scouting_info = []

    with open(filePath,'r') as file:
        lines = file.readlines()
        
        for line in lines:
            line_array = line.split('\t')
            line_info = DotDict()
            line_info['key'] = 'frc' + str(line_array[5])
            line_info['initials'] = line_array[0]
            line_info['event'] = line_array[1]
            line_info['match_level'] = line_array[2]
            line_info['match_number'] = line_array[3]
            line_info['robot_number'] = line_array[4]
            line_info['team_number'] = line_array[5]
            line_info['auto_start_position'] = line_array[6]
            line_info['left_starting_zone'] = line_array[7]
            line_info['auto_amp_score'] = line_array[8]
            line_info['auto_speaker_score'] = line_array[9]
            line_info['teleop_amp_score'] = line_array[10]
            line_info['teleop_speaker_score'] = line_array[11]
            line_info['times_amplified'] = line_array[12]
            line_info['pickup_from'] = line_array[13]
            line_info['climb_time'] = line_array[14]
            line_info['climb_status'] = line_array[15]
            line_info['trap_status'] = line_array[16]
            line_info['driver_skill'] = line_array[17]
            line_info['defense_rating'] = line_array[18]
            line_info['speed_rating'] = line_array[19]
            line_info['immobilized'] = line_array[20]
            line_info['tippy'] = line_array[21]
            line_info['dropped_notes_status'] = line_array[22]
            line_info['good_partner'] = line_array[23]
            line_info['comment'] = line_array[24].rstrip('\n')
            line_info = DotDict(line_info)
            scouting_info.append(line_info)
    return scouting_info

def getAllPitInfoList(filePath):
    all_lines = []

    with open(filePath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_array = line.split('\t')
            #If the line is from match scouting, skip it
            if line_array[0] == 'm':
                continue
            line_array[len(line_array)-1] = line_array[len(line_array)-1].rstrip('\n')
            line_array = line_array[1:]
            all_lines.append(line_array)

    return all_lines

def updatePitScoutingFile(allDataPath,pitDataPath):
    line_arr = []
    # Get match data from all scouting data
    with open(allDataPath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line[0] != 'p': continue
            line_arr.append(line[2:])
    #Clear File
    with open(pitDataPath, 'w') as file: pass
    #Rewrite all pit data
    with open(pitDataPath, 'a') as file:
        for line in line_arr:
            file.write(line)
    return

path1 = 'py/app/data/all_scouting_data.txt'
path2 = 'py/app/data/pit_scouting_data.txt'
updatePitScoutingFile(path1,path2)
