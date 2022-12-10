date = 2022
player_path = "playerS.csv"
goals_path = "goals.csv"
teams_path = "teams.csv"
matches_path = "matches.csv"
manager_path = "managers.csv"
manager_apperances_path = "manager_appearances.csv"
referee_path = "referees.csv"
referee_appearances_path = "referee_appearances.csv"
def reader(full_path:str,target:str,target_indexes:list,action,break_at_end = False):
    file = open(full_path,'r',encoding="utf8")
    file.readline()
    while True:
        line = file.readline()
        if line == "": break
        line = line.split(',')
        continue_ = True
        for target_index in target_indexes:
            print(line[target_index])
            if line[target_index] == target:
                continue_ = False
        if continue_: continue
        action(line)
        if (break_at_end): break
    file.close()
def player_profile(path:str,target:str):
    output = {}
    def act1(line:list):
        output['lastname'] = line[1]
        output['firstname'] = line[2]
        output['age'] = date - int(line[3].split('-')[0])
        output['games played'] = int(line[8])
        output['fifa appearances'] = line[9].split('.')
    reader(path+player_path,target,[0],act1,True)
    #searching for goals count
    output['goals count'] = 0
    def act2(line:list):
        output['goals count'] += 1
    reader(path+goals_path,target,[8],act2)
    return output
def team_profile(path:str,target:str):
    output = {}
    def act1(line:list):
        output['name'] = line[1]
        output['code'] = line[2]
        output['region'] = line[3]
    reader(path+teams_path,target,[0],act1,True)
    output['games played'] = 0
    output['fifa years'] = []
    output['wins'] = 0
    output['loses'] = 0
    output['ties'] = 0
    def act2(line:list):
        output['games played'] += 1
        if not line[8].split('-')[0] in output['fifa years']:
            output['fifa years'].append(line[8].split('-')[0])
        if line[27] == '1':
            output['ties'] += 1
        elif line[26] == '1':
            if target == line[14]:
                output['loses'] += 1
            elif target == line[15]:
                output['wins'] += 1
        elif line[27] == '1':
            if target == line[14]:
                output['wins'] += 1
            elif target == line[15]:
                output['loses'] += 1
    reader(path+matches_path,target,[14,15],act2)
    return output
def manager_profile(path:str,target:str):
    output = {}
    def act1(line:list):
        output['lastname'] = line[1]
        output['firstname'] = line[2]
        output['region'] = line[3]
    reader(path+manager_path,target,[0],act1,True)
    output['teams managed'] = 'no data regarding to it'
    output['games played'] = 0
    games_ids = []
    def act2(line:list):
        games_ids.append(line[0])
        output['games played'] += 1
    #nemidonam chera, valy vaghty dare manager_appearances ro 
    #mikhoneh, hich vorodi ro ghabol nemikone
    #ba print check kardam, nemidnam chera valy M-000 ro age vorody
    #bedim, agar to file ham bashe baz adam hesabsh nemikone va mige
    #(line[2] == "M-000") = ("M-000" == "M-000") = False
    #in bag vagaht va faghat hengam khandan as file manager_appearances
    #rokh mide, jaleb tar inke agar mored akhar manager_appearances ro
    #vorodi bedahid, kar mecone
    reader(path+manager_apperances_path,target,[2],act2)
    output['years'] = []
    def act3(line:list):
        if not line[8].split('-')[0] in output['years']:
            output['years'].append(line[8].split('-')[0])
    reader(path+matches_path,target,[0],act3)
    return output
def referee_profile(path:str,target:str):
    output = {}
    def act1(line:list):
        output['lastname'] = line[1]
        output['firstname'] = line[2]
        output['region'] = line[3]
    reader(path+referee_path,target,[0],act1,True)
    output['games played'] = 0
    game_ids = []
    def act2(line:list):
        output['games played'] += 1
        game_ids.append(line[0])
    reader(path+referee_appearances_path,target,[2],act2)
    def act3(line:list):
        if not line[8].split('-')[0] in output['years']:
            output['years'].append(line[8].split('-')[0])
    reader(path+matches_path,target,[0],act3)
    #moshkel manager_appearances inja ham rokh mide
    return output