import sys, heapq

N, M = map(int, str.rstrip(sys.stdin.readline(), '').split(' '))
numbers = [int(str.rstrip(sys.stdin.readline(), '')) for _ in range(N)]
arr = [[(-1, -1) for _ in range(N//2)] for _ in range(N)]
for a in range(N):
    for b in range(a, N):
        if a == b :
            arr[a][b] = (numbers[a], numbers[a])
        else :
            arr[a][b] = (min(numbers[b], arr[a][b-1][0]), max(numbers[b], arr[a][b-1][1]))
range_list = [zip(map(int, str.rstrip(sys.stdin.readline(), '').split(' '))) for _ in range(M)]
for a, b in range_list:
    a = a[0] - 1
    b = b[0] - 1
    print(arr[a][b][0], arr[a][b][1])
