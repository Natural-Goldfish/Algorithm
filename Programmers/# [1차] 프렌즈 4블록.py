def check(arr):
    block_num, flag = 0, False
    for y in range(len(arr)-1):
        for x in range(len(arr[0])-1):
            if arr[y][x][0] == 'b' : continue
            i, r, d, rd = arr[y][x][0], arr[y][x+1][0], arr[y+1][x][0], arr[y+1][x+1][0]
            if i==r and i==d and i==rd :
                block_num += 4 - len(list(filter(lambda x : x, [arr[y][x][1], arr[y][x+1][1], arr[y+1][x][1], arr[y+1][x+1][1]])))
                arr[y][x], arr[y][x+1], arr[y+1][x], arr[y+1][x+1] = (i, True), (r, True), (d, True), (rd, True)
                flag = True
    if not flag : 
        return block_num, False
    else : 
        return block_num, True

def destroy(arr):
    new_arr = [[('b', False) for _ in range(len(arr[0]))] for _ in range(len(arr))]
    for x in range(len(arr[0])):
        temp = []
        for y in range(len(arr)):
            if not arr[y][x][1] and arr[y][x][0] != 'b' : temp.append(arr[y][x])
        if not temp : continue
        index = 0
        for y in range(len(new_arr)-len(temp), len(new_arr)):
            new_arr[y][x] = temp[index]
            index += 1
    return new_arr
            
def solution(m, n, board):  # H, W, arr
    arr = []
    for row in board:
        arr.append([(char, False) for char in map(lambda x : x, row)])
    answer = 0
    while True:
        num, flag = check(arr)
        if not flag : break
        answer += num
        arr = destroy(arr)
    return answer