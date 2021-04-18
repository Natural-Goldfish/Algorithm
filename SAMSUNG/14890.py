global N, MIN_REQUIRED_NUM

def check(arr, reverse=False):
    global N, MIN_REQUIRED_NUM
    init_index = 0 if not reverse else -1
    init_loop_index = 1 if not reverse else len(arr)-2
    end_loop_index = len(arr) if not reverse else -1
    jump = 1 if not reverse else -1
    cur_value = arr[0] if not reverse else arr[-1]
    cur_value_count = 1

    decrease = False
    for index in range(init_loop_index, end_loop_index, jump):
        next_value = arr[index]
        d = next_value - cur_value

        if d < -1 : return False
        elif d == -1 :
            if not decrease :
                cur_value = next_value
                cur_value_count = 1
                decrease = True
            else :
                if cur_value_count >= MIN_REQUIRED_NUM :
                    cur_value = next_value
                    cur_value_count = 1
                else :
                    return False
        elif d == 0 :
            cur_value_count += 1
        elif d == 1 :
            if not decrease :
                if cur_value_count >= MIN_REQUIRED_NUM :
                    cur_value = next_value
                    cur_value_count = 1
                    decrease = False
                else : return False
            else :
                if cur_value_count >= MIN_REQUIRED_NUM * 2 :
                    cur_value = next_value
                    cur_value_count = 1
                    decrease = False
                else : return False
        else :
            return False
    if decrease :
        if cur_value_count < MIN_REQUIRED_NUM : return False
    return True
        
if __name__ == "__main__":
    N, MIN_REQUIRED_NUM = map(int, input().rstrip().split(' '))
    load_map, possible_load = [], 0
    for n in range(N):
        load_map.append(list(map(int, input().rstrip().split(' '))))
    
    for y in range(N):
        result = check(load_map[y])
        result_reverse = check(load_map[y], True)
        if not result and not result_reverse : continue
        possible_load += 1

    for x in range(N):
        temp_map = []
        for y in range(N):
            temp_map.append(load_map[y][x])
        result = check(temp_map)
        result_reverse = check(temp_map, True)
        if not result and not result_reverse : continue
        possible_load += 1

    print(possible_load)
    