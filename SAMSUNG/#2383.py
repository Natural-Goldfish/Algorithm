from collections import deque
from itertools import product

global stair_info

def cal(cur_case):
    global stair_info
    s1_input_list, s2_input_list = [], []
    for coords in cur_case:
        user_coord, stair_coord = coords
        uy, ux = user_coord
        sy, sx = stair_coord

        sid = stair_info[(sy, sx)]['id']
        d = abs(sy- uy) + abs(sx - ux)
        if sid == 1 :
            s1_input_list.append(d+1)
        else :
            s2_input_list.append(d+1)

    s1_input_list.sort(), s2_input_list.sort()
    s1_list, s2_list = deque(s1_input_list), deque(s2_input_list)

    s1_id, s2_id = -1, -1
    for sid, item in stair_info.items():
        if item['id'] == 1 :
            s1_id = sid
        else :
            s2_id = sid
    time = 0
    while True :

        s1f, s2f = stair_info[s1_id]['list'].popleft(), stair_info[s2_id]['list'].popleft()
        if s1f :
            stair_info[s1_id]['on-people'] -= len(s1f)
        if s2f :
            stair_info[s2_id]['on-people'] -= len(s2f)

        s1_possible_people_num = stair_info[s1_id]['max-people'] - stair_info[s1_id]['on-people']
        s1_arrive_list = []
        for _ in range(s1_possible_people_num):
            if s1_list :
                if s1_list[0] <= time :
                    s1_arrive_list.append(s1_list.popleft())
                else : break
            else : break

        if s1_arrive_list :
            stair_info[s1_id]['list'].append(s1_arrive_list)
            stair_info[s1_id]['on-people'] += len(s1_arrive_list)
        else :
            stair_info[s1_id]['list'].append([])

        s2_possible_people_num = stair_info[s2_id]['max-people'] - stair_info[s2_id]['on-people']
        s2_arrive_list = []
        for _ in range(s2_possible_people_num):
            if s2_list :
                if s2_list[0] <= time :
                    s2_arrive_list.append(s2_list.popleft())
                else : break
            else : break
        if s2_arrive_list :
            stair_info[s2_id]['list'].append(s2_arrive_list)
            stair_info[s2_id]['on-people'] += len(s2_arrive_list)
        else :
            stair_info[s2_id]['list'].append([])


        if not s1_list and not s2_list and stair_info[s1_id]['on-people'] == 0 and stair_info[s2_id]['on-people'] == 0:
            break
    
        time += 1
    return time

if __name__ == "__main__":
    T = int(input().rstrip())
    for test_case in range(1, T+1):
        N = int(input().rstrip())
        H, W = N, N
        arr = []
        for y in range(N):
            arr.append(list(map(int, input().rstrip().split(' '))))
        
        user_list, stair_list= [], []
        stair_info, stair_id = {}, 1
        for y in range(len(arr)):
            for x in range(len(arr[0])):
                if arr[y][x] == 1 :
                    user_list.append([(y, x)])
                elif arr[y][x] == 0 : continue
                else :
                    stair_list.append((y, x))
                    stair_info[(y, x)] = {
                        'id' : stair_id,
                        'max-people' : 3,
                        'on-people' : 0,
                        'list' : deque([[] for _ in range(arr[y][x])])
                    }
                    stair_id += 1
        
        temp_set = []
        for user in user_list:
            # [(user1_coord, stair1_coord), (user1, stair2_coord)]
            temp_set.append(list(product(*[user, stair_list])))
        
        
        possible_cases = product(*temp_set)         #((user1_coord, stair2_coord), (user2_coord, stair1_coord) ...)
        min_time = 9999999999999
        for possible_case in possible_cases:
            time = cal(possible_case)
            min_time = min(time, min_time)

        print("#{} {}".format(test_case, min_time))