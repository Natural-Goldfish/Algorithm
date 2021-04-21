
global MIN_REQUIRED_NUM, arr

def search():
    count = 0
    # 세로
    for x in range(len(arr[0])):
        temp_list = []              # 세로 리스트
        for y in range(len(arr)):
            temp_list.append(arr[y][x])
        if check(temp_list):             # 가능 여부 판단
            count += 1

    # 가로
    for y in range(len(arr)):
        if check(arr[y]) :             # 가능 여부 판단
            count +=1
    
    return count

def check(temp_list):
    global MIN_REQUIRED_NUM
    i_flag, d_flag = False, False
    cur_height = temp_list[0]
    cur_value_info = (cur_height, 1)
    for index in range(1, len(temp_list)) :
        next_height = temp_list[index]
        cur_height, cur_value_count = cur_value_info
        dh = next_height - cur_height

        if dh < -1 :    # 1칸 이상 차이나는 경우
            return False
        elif dh == -1 : # 뒤에가 낮음
            if d_flag :
                # 최소기준  만족하는지 검사
                if cur_value_count < MIN_REQUIRED_NUM :
                    return False
                else :
                    d_flag = True
                    cur_value_info = (next_height, 1)
                    continue
            else :
                d_flag = True
                cur_value_info = (next_height, 1)
                continue
        elif dh == 0 :    # 높이가 같은 경우
            cur_value_info = (cur_height, cur_value_count+1)
            continue
        elif dh == 1:   # 다음이 1칸 높은 경우
            if d_flag:
                # 최소 기준의 두배 만족하는지 검사
                if cur_value_count < MIN_REQUIRED_NUM*2 : return False
                else :
                    d_flag = False
                    cur_value_info = (next_height, 1)
                    continue
            else :
                # 최소기준 만족
                if cur_value_count < MIN_REQUIRED_NUM : return False
                else :
                    cur_value_info = (next_height, 1)
                    continue
        elif dh > 1 :   # 1칸 이상 차이나는 경우
            return False

    if d_flag:
        _, count = cur_value_info
        if count < MIN_REQUIRED_NUM :
            return False
    return True


if __name__ == "__main__":
    T = int(input().rstrip())
    for test_case in range(1, T + 1):
        N, L = map(int, input().rstrip().split(' '))
        MIN_REQUIRED_NUM = L
        arr = []
        for y in range(N):
            arr.append(list(map(int, input().rstrip().split(' '))))

        print("#{} {}".format(test_case, search()))