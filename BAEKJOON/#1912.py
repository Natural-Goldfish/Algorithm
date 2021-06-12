def solution(N, Array):
    if N == 1 : print(Array[0])
    else :
        newArray = []
        curSum = 0

        if Array[0] <= 0 : flag = True
        else : flag = False

        for idx, value in enumerate(Array) :
            if value > 0 :
                if flag == False :
                    curSum += value
                else :
                    flag = False
                    newArray.append(curSum)
                    curSum = value

            else :
                if flag == False :
                    flag = True
                    newArray.append(curSum)
                    curSum = value
                else :
                    curSum += value

            if idx == len(Array) - 1 :
                newArray.append(curSum)

        if len(newArray) == 1 and newArray[0] > 0 : print(newArray[0])
        else :
            startPoint = -1
            for i in range(len(newArray)):
                if newArray[i] > 0 :
                    startPoint = i
                    break
            if startPoint == -1 :
                print(max(Array))
            else :
                for i in range(startPoint + 2, len(newArray), 2):
                  if max(newArray[i - 2] + newArray[i - 1] + newArray[i], newArray[i]) != newArray[i]:
                    newArray[i] = newArray[i - 2] + newArray[i - 1] + newArray[i]
                print(max(newArray))
                    
        
if __name__ == "__main__":
    n = int(input())
    
    array = list(map(int, input().split(" ")))
    solution(n, array)