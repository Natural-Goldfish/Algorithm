import sys
from collections import deque

N = int(str.strip(sys.stdin.readline()))
target1, target2 = map(int, str.strip(sys.stdin.readline()).split(' '))
people_dict = {parent : [] for parent in range(N+1)}
M = int(str.strip(sys.stdin.readline()))
for m in range(M):
    person1, person2 = map(int, str.strip(sys.stdin.readline()).split(' '))
    people_dict[person1].append(person2)
    people_dict[person2].append(person1)

def bfs(start, target, people_dict):
    visited = set([])
    queue = deque([start])
    relation = 0
    while queue :
        temp_queue = []
        while queue :
            cur = queue.popleft()
            if cur == target : 
                return relation
            if cur in visited : continue
            visited.add(cur)

            for person in people_dict[cur]:
                temp_queue.append(person)
            
        if temp_queue :
            queue = deque(temp_queue)
            relation += 1
    return -1
print(bfs(target1, target2, people_dict))