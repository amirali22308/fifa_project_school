matches_path = "matches.csv"
def compare(path:str,target1:str,target2:str):
    file = open(path+matches_path,'r',encoding="utf8")
    keys = file.readline().split(',')
    output = []
    while True:
        line = file.readline()
        if line == "": break
        line = line.split(',')
        if line[14] == target1 or line[15] == target2:
            if line[15] == target1 or line[15] == target2:
                new_item = {}
                for turn in range(len(keys)):
                    new_item[keys[turn]] = line[turn]
                output.append(new_item)
    file.close()
    return output