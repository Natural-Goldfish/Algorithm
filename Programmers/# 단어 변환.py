def solution(begin, target, words):
    answer = 0
    visited = [0]*len(words)
    length = len(words[0])
    if target not in words :
        return answer
    else :
        answer = BFS(begin, target, words, visited, length)
    return answer

def BFS(begin, target, words, visited, length):
    queue = [begin, -1]
    count = 0
    while queue :
        curWord = queue.pop(0)
        if curWord == begin : pass
        elif curWord == target : return count
        elif curWord == -1 : 
            count += 1
            continue
        else :
            if visited[words.index(curWord)] == 1 : continue
            visited[words.index(curWord)] = 1
        
        for i in range(len(words)):
            if visited[i] == 0 :
                flag = True
                for j in range(length):
                    if words[i][j] != curWord[j] :
                        for k in range(length):
                            if j == k : pass
                            elif words[i][k] == curWord[k]: pass
                            else : 
                                flag = False
                                break
                        if flag : queue.append(words[i])                                      

        if len(queue) == 0 : return 0
        elif queue[0] == -1 : 
            queue.append(-1)
    return 0