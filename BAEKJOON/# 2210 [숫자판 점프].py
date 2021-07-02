import sys

H, W = 5, 5

arr = list(list(map(int, str.strip(sys.stdin.readline()).split(' '))) for _ in range(H))
answers = set([])

def dfs(arr, coord, numbers):
    y, x = coord
    numbers.append(str(arr[y][x]))

    if len(numbers) == 6 :
        answers.add(''.join(numbers))
        numbers.pop()
        return

    for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)] :
        if y+dy < 0 or y+dy >= H or x+dx < 0 or x+dx >= W : continue
        dfs(arr, (y+dy, x+dx), numbers)
    
    numbers.pop()
    return

for y in range(H):
    for x in range(W):
        dfs(arr, (y, x), [])
print(len(answers))