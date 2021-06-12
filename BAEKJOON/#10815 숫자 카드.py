def solution(N, NList, M, MList):
    userDict = {}
    returnList = []
    for value in NList:
        userDict[value] = True
    
    for value in MList :
        try :
            if userDict[value] == True :
                returnList.append(1)
                print(1, end = " ")
        except :
            returnList.append(0)
            print(0, end = " ")
    

if __name__ == "__main__":
    N = int(input())
    NList = list(map(int, input().split(' ')))
    M = int(input())
    MList = list(map(int, input().split(' ')))
    solution(N, NList, M, MList)