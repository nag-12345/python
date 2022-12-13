def swappositions(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list
list = [4,7,1,9]
pos1,pos2=2,3
print(swappositions(list,pos1-1,pos2-1))
