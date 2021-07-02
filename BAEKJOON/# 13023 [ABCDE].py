import sys

N, M = map(int, str.strip(sys.stdin.readline()).split(' '))
friends_dict = {friend : [] for friend in range(N)}
for m in range(M):
    a, b = map(int, str.strip(sys.stdin.readline()).split(' '))
    friends_dict[a].append(b)
    friends_dict[b].append(a)

flag = False
def dfs(person, visited, count, friends_dict):
    global flag

    visited.add(person)
    count += 1

    if count == 5 :
        flag = True

    for friend in friends_dict[person]:
        if friend in visited : continue
        if not flag :
            dfs(friend, visited, count, friends_dict)
    
    visited.remove(person)

for person in range(N):
    if not flag :
        dfs(person, set([]), 0, friends_dict)
    if flag : break
if flag : print(1)
else : print(0)