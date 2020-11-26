from itertools import combinations

def solution(clothes):
    clothesDict = {}
    num = 1
    for i in range(len(clothes)):
        if clothes[i][1] in clothesDict.keys() :
            clothesDict[clothes[i][1]].append(clothes[i][0])
        else :
            clothesDict[clothes[i][1]] = [clothes[i][0]]
                                                     

    for key, values in clothesDict.items():
        length = len(values)
        num *= (length + 1)
        
    return num - 1