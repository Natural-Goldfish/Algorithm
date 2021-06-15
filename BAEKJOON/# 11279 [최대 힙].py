import sys, heapq

N = int(str.rstrip(sys.stdin.readline(), ''))
heap, answer = [], []
for _ in range(N):
    number = int(str.rstrip(sys.stdin.readline(), ''))
    if number == 0:
        if heap :
            answer.append(-heapq.heappop(heap))
        else :
            answer.append(0)
    else :
        heapq.heappush(heap, -number)
for number in answer :
    print(number)
