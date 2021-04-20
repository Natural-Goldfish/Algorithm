global arr, H, W, coord_dict
'''
(-2, -2, -2) : 빈 공간
(1, x, t) : 활성화
(0, x, t) : 비활성화
(-1, -1, -1) : 죽음
'''

def spread():
    global arr, coord_dict

    for y in range(len(arr)):
        for x in range(len(arr[0])):
            flag, value, time = arr[y][x]
            if flag == 1 :
                # UP
                new_y, new_x = y-1, x
                if new_y < 0 or new_y >= len(arr) :     # 탐색 공간 벗어남
                    if (new_y, new_x) in coord_dict :   # 다른 세포에서 먼저 온 경우
                        if max(coord_dict[(new_y, new_x)][1], (0, value, 0)[1]) == value :
                            coord_dict[(new_y, new_x)] = (0, value, 0)
                    else :                              # 내가 처음
                        coord_dict[(new_y, new_x)] = (0, value, 0)
                else :
                    flag_a, value_a, time_a = arr[new_y][new_x]
                    if flag_a == -2 :
                        if (new_y, new_x) in coord_dict :                        
                            if max(coord_dict[(new_y, new_x)][1], (0, value, 0)[1]) == value :
                                coord_dict[(new_y, new_x)] = (0, value, 0)
                        else :
                            coord_dict[(new_y, new_x)] = (0, value, 0)

                # Down
                new_y, new_x = y+1, x
                if new_y < 0 or new_y >= len(arr) :     # 탐색 공간 벗어남
                    if (new_y, new_x) in coord_dict :   # 다른 세포에서 먼저 온 경우
                        if max(coord_dict[(new_y, new_x)][1], (0, value, 0)[1]) == value :
                            coord_dict[(new_y, new_x)] = (0, value, 0)
                    else :                              # 내가 처음
                        coord_dict[(new_y, new_x)] = (0, value, 0)
                else :
                    flag_a, value_a, time_a = arr[new_y][new_x]
                    if flag_a == -2 :
                        if (new_y, new_x) in coord_dict :
                            if max(coord_dict[(new_y, new_x)][1], (0, value, 0)[1]) == value :
                                coord_dict[(new_y, new_x)] = (0, value, 0)
                        else :
                            coord_dict[(new_y, new_x)] = (0, value, 0)

                # Left
                new_y, new_x = y, x-1
                if new_x < 0 or new_x >= len(arr[0]) :     # 탐색 공간 벗어남
                    if (new_y, new_x) in coord_dict :   # 다른 세포에서 먼저 온 경우
                        if max(coord_dict[(new_y, new_x)][1], (0, value, 0)[1]) == value :
                            coord_dict[(new_y, new_x)] = (0, value, 0)
                    else :                              # 내가 처음
                        coord_dict[(new_y, new_x)] = (0, value, 0)
                else :
                    flag_a, value_a, time_a = arr[new_y][new_x]
                    if flag_a == -2 :
                        if (new_y, new_x) in coord_dict :
                            if max(coord_dict[(new_y, new_x)][1], (0, value, 0)[1]) == value :
                                coord_dict[(new_y, new_x)] = (0, value, 0)
                        else :
                            coord_dict[(new_y, new_x)] = (0, value, 0)
                # Right
                new_y, new_x = y, x+1
                if new_x < 0 or new_x >= len(arr[0]) :     # 탐색 공간 벗어남
                    if (new_y, new_x) in coord_dict :   # 다른 세포에서 먼저 온 경우
                        if max(coord_dict[(new_y, new_x)][1], (0, value, 0)[1]) == value :
                            coord_dict[(new_y, new_x)] = (0, value, 0)
                    else :                              # 내가 처음
                        coord_dict[(new_y, new_x)] = (0, value, 0)
                else :
                    flag_a, value_a, time_a = arr[new_y][new_x]
                    if flag_a == -2 :
                        if (new_y, new_x) in coord_dict :
                            if max(coord_dict[(new_y, new_x)][1], (0, value, 0)[1]) == value :
                                coord_dict[(new_y, new_x)] = (0, value, 0)
                        else :
                            coord_dict[(new_y, new_x)] = (0, value, 0)
    if coord_dict :
        new_arr = [[(-2, -2, -2) for _ in range(len(arr[0])+2)]]
        for y in range(len(arr)):
            temp = [(-2, -2, -2)] + arr[y] +[(-2, -2, -2)]
            new_arr.append(temp)
        new_arr.append([(-2, -2, -2) for _ in range(len(arr[0])+2)])

        for coord, value in coord_dict.items() :
            y, x = coord
            new_arr[y+1][x+1] = value
        arr = new_arr
        new_arr = None

def one_second():
    global arr, coord_dict
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if (y-1, x-1) in coord_dict : continue

            flag, value, time = arr[y][x]
            if flag == -1 or flag == -2 : continue

            if flag == 1 :
                if time+1 == value :      # 수명 끝
                    arr[y][x] = (-1, -1, -1)
                else :
                    arr[y][x] = (flag, value, time+1)
            elif flag == 0 :
                if time+1 == value :      # 삶을 시작
                    arr[y][x] = (1, value, 0)
                else :
                    arr[y][x] = (0, value, time+1)
    coord_dict = {}

coord_dict = {}

if __name__ == "__main__":
    T = int(input().rstrip())
    for test_case in range(1, T+1):
        H, W, K = map(int, input().rstrip().split(' '))
        arr = [[(-2, -2, -2) for _ in range(W)] for _ in range(H)]
        for y in range(H):
            temp = list(map(int, input().rstrip().split(' ')))
            for x, item in enumerate(temp) :
                if item != 0 :
                    arr[y][x] = (0, item, 0)
                    
        k = 0
        while k != K :
            spread()
            one_second()
            k += 1
        count = 0
        for y in range(len(arr)):
            for x in range(len(arr[0])):
                if arr[y][x][0] == 1 or arr[y][x][0] == 0 :
                    count += 1
        print("#{} {}".format(test_case, count))