def search(target:str,path:str,target_index1:int,wanted_start:int,wanted_end:int,target_index2=None):
    file = open(path,'r',encoding="utf8")
    file.readline()
    output = []
    while True:
        line = file.readline()
        if line == "": break
        line = line.split(',')
        if target in line[target_index1]:
             output.append(line[wanted_start : wanted_end+1])
        elif target_index2 != None:
            if target in line[target_index2]:
             output.append(line[wanted_start : wanted_end+1])
    file.close()
    return output