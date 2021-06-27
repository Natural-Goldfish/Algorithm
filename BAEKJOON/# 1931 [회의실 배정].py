import sys
N = int(str.rstrip(sys.stdin.readline()))
answer = 1
arr = sorted([list(map(int, str.rstrip(sys.stdin.readline()).split(' '))) for _ in range(N)], key=lambda x : (x[1], x[0]))
end_time = arr[0][1]

for item in arr[1:]:
    if item[0] < end_time : continue
    end_time = item[1]
    answer += 1
print(answer)


