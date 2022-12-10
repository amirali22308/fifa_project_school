from search import search
goals_path = "goals.csv"
matches_path = "matches.csv"
players_path = "players.csv"
teams_path = "teams.csv"
def year_check(year:int,target:str,path:str)->bool:
    file = open(path+matches_path,'r',encoding="utf8")
    file.readline()
    while True:
        line = file.readline()
        if line == "": break
        line = line.split(',')
        if line[0] != target: continue
        file.close()
        return int(line[8].split('-')[0]) == year
    file.close()
    return False
def best_goaler(path:str,year=None):
    file = open(path+goals_path,'r',encoding="utf8")
    file.readline()
    goals = {}
    best = ("None",0)
    while True:
        line = file.readline()
        if line == "": break
        line = line.split(',')
        if (year != None):
            if (not year_check(year,line[1],path)):
                continue
        if line[8] in goals:
            goals[line[8]] += 1
        else:
            goals[line[8]] = 0
        if goals[line[8]] > best[1]:
            best = (line[8],goals[line[8]])
    file.close()
    print(best[0])
    return search(best[0],path+players_path,0,0,2)[0]
def goals_check(path:str,reverse=False,year=None):
    '''
    defualt is attack
    reverse is taken
    '''
    file = open(path+matches_path,'r',encoding="utf8")
    file.readline()
    goals_taken = {}
    def read_goals(line:list):
        t1 = (line[14],int(line[17]))
        t2 = (line[15],int(line[18]))
        if reverse:
            holder = t1
            t1 = t2
            t2 = holder
        if t1[0] in goals_taken:
            goals_taken[t1[0]] += t1[1]
        else:
            goals_taken[t1[0]] = t1[1]
        if t2[0] in goals_taken:
            goals_taken[t2[0]] += t2[1]
        else:
            goals_taken[t2[0]] = t2[1]
        return t1[0],t2[0]
    output = None
    while True:
        line = file.readline()
        if line == "": break
        line = line.split(',')
        if year != None: 
            if int(line[8].split('-')[0]) != year:
                continue
        t1,t2 = read_goals(line)
        if output == None:
            if (int(goals_taken[t1]) > int(goals_taken[t2])) and not reverse: output = t1
            else: output = t2
        else:
            if int(goals_taken[t1]) > int(goals_taken[output]) and not reverse: output = t1
            if int(goals_taken[t2]) > int(goals_taken[output]) and not reverse: output = t2
    file.close()
    return search(output,path+teams_path,0,0,2)