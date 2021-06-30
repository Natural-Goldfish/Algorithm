import sys, heapq

N, M = map(int, str.strip(sys.stdin.readline()).split(' '))

relation_dict = {person : [] for person in range(N+1)}

for m in range(M):
    person1, person2 = map(int, str.strip(sys.stdin.readline()).split(' '))
    relation_dict[person1].append(person2)
    relation_dict[person2].append(person1)

def dijkstra(person, relation_dict, N) :
    distances = [sys.maxsize for _ in range(N+1)]
    distances[person] = 0
    heap = [(0, person)]

    while heap :
        _, cur = heapq.heappop(heap)

        for person in relation_dict[cur]:
            if distances[cur] + 1 < distances[person] :
                distances[person] = distances[cur] + 1
                heapq.heappush(heap, (distances[person], person))
    return sum(distances[1:])
answer = (sys.maxsize, sys.maxsize)
for person in range(1, N+1):
    distance = dijkstra(person, relation_dict, N)
    if distance < answer[0] :
        answer = (distance, person)
print(answer[1])