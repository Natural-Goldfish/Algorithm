

global arr, DIRECTION
# 
DIRECTION = {
    1 : (-1, 0),    #상
    2 : (1, 0),     #하
    3 : (0, -1),    #좌
    4 : (0, 1)      #우
}
def move():
    global arr
    '''
    1시간 단위로 지정된 방향으로 이동
    새로운 배열 생성
    '''
    new_arr = [[[] for _ in range(len(arr[0]))] for _ in range(len(arr))]
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            # 약품 위치 
            # x : 0, len(arr[0])-1
            # y : 0, len(arr)-1
            if not arr[y][x] : continue
            n, d = arr[y][x][0]
            dy, dx = DIRECTION[d]
            new_y, new_x = y + dy, x + dx

            if new_y == 0 or new_y == len(arr)-1 or new_x == 0 or new_x == len(arr[0])-1 : # 미생물 감소            
                new_n = n//2
                if new_n == 0 :
                    new_arr[new_y][new_x] = []
                    continue
                else :
                    if d%2 == 0 :
                        new_d = d-1
                    else :
                        new_d = d+1
                    new_arr[new_y][new_x].append((new_n, new_d))
                    continue
            else :
                new_arr[new_y][new_x].append((n, d))
    arr = new_arr
    new_arr = None

def summary():
    global arr
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if not arr[y][x] : continue
            temp_list = arr[y][x]

            if len(temp_list) == 1 :
                continue
            elif len(temp_list) > 1 :
                n_list = [item[0] for item in temp_list]
                d_list = [item[1] for item in temp_list]
                new_d = d_list[n_list.index(max(n_list))]
                new_n = sum(n_list)

                if new_n == 0 :
                    arr[y][x] = []
                    continue
                arr[y][x] = [(new_n, new_d)]


if __name__ == "__main__":
    T = int(input().rstrip())
    for test_case in range(1, T + 1):
        N, time, K = map(int, input().rstrip().split(' '))
        arr = [[[] for _ in range(N)] for _ in range(N)]

        for k in range(K):
            y, x, n, d = map(int, input().rstrip().split(' '))
            arr[y][x].append((n, d))
        
        for t in range(time):
            move()
            summary()
        answer = 0
        for y in range(len(arr)):
            for x in range(len(arr[0])):
                if not arr[y][x] : continue
                answer += sum([ x[0] for x in arr[y][x]])

        print("#{} {}".format(test_case, answer))
