import sys, heapq

N = int(str.rstrip(sys.stdin.readline(), ''))
heap = []
command = list([int(str.rstrip(sys.stdin.readline(), '')) for _ in range(N)])
for index in range(N):
    if command[index] == 0 and heap : 
        print(heapq.heappop(heap))
    elif command[index] == 0 :
        print(0)
    else :
        heapq.heappush(heap, command[index])