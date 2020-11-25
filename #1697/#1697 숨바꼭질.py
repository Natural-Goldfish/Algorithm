def solution(N, K, visited):
    toVisit = [N]
    time = 0
    while toVisit :
        tempArray = []
        for i in range(len(toVisit)):
            curPoint = toVisit[i]
            if curPoint == K : break
            if visited[curPoint] == 0 :
                temp = search(curPoint, visited)
                if temp == None : pass
                else : tempArray.extend(temp)

        if curPoint == K : break

        toVisit = tempArray
        if len(toVisit) == 0 : break
        else : time += 1

    print(time)

def search(curPoint, visited):
    visited[curPoint] = 1        
    temp = []

    # WALK - LEFT
    if curPoint - 1 < 0 : pass
    else :
        if visited[curPoint -1] == 0 : temp.append(curPoint - 1)
    # WALK - RIGHT
    if curPoint + 1 >= len(visited) : pass
    else :
        if visited[curPoint + 1] == 0 : temp.append(curPoint + 1)
    # BLINK
    if (curPoint * 2) >= len(visited) : pass
    else :
        if visited[curPoint * 2] == 0 : temp.append(curPoint * 2)
    
    if len(temp) == 0 : return None
    else : return temp

if __name__ == "__main__":
    N, K = map(int, input().split(" "))
    visited = [0]*100001
    solution(N, K, visited)