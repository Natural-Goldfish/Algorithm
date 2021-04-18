import sys
def r_sort(arr):
    max_length = 0
    for y in range(len(arr)):
        temp_dict = {}
        temp_list = []
        for number in arr[y]:
            if number == 0 : continue
            if number not in temp_dict :
                temp_dict[number] = 1
            else :
                temp_dict[number] += 1
        for number, count in temp_dict.items():
            temp_list.append((number, count))
        arr[y] = []
        temp_list.sort(key = lambda x : (x[1], x[0]))
        for number, count in temp_list:
            arr[y].append(number)
            arr[y].append(count)
        max_length = max(len(arr[y]), max_length)
    for y in range(len(arr)):
        if len(arr[y]) != max_length :
            for i in range(max_length-len(arr[y])):
                arr[y].append(0)

def c_sort(arr):
    max_length = len(arr)
    for x in range(len(arr[0])):
        target_list = []
        for y in range(len(arr)):
            if arr[y][x] != 0 :
                target_list.append(arr[y][x])
        temp_dict = {}
        temp_list = []
        for number in target_list:
            if number not in temp_dict :
                temp_dict[number] = 1
            else :
                temp_dict[number] += 1
        for number, count in temp_dict.items():
            temp_list.append((number, count))
        temp_list.sort(key = lambda x : (x[1], x[0]))
        cur_length = len(temp_list)*2
        index_y = 0
        if cur_length < max_length :
            for number, count in temp_list:
                arr[index_y][x] = number
                index_y += 1
                arr[index_y][x] = count
                index_y += 1
            for index in range(index_y, max_length):
                arr[index][x] = 0
        elif cur_length == max_length :
            for number, count in temp_list:
                arr[index_y][x] = number
                index_y += 1
                arr[index_y][x] = count
                index_y += 1
        else :
            for i in range(cur_length- max_length):
                arr.append([0 for j in range(len(arr[0]))])
            for number, count in temp_list:
                arr[index_y][x] = number
                index_y += 1
                arr[index_y][x] = count
                index_y += 1      

        max_length = max(cur_length, max_length)

if __name__ == "__main__":

    target_y, target_x, target = map(int, sys.stdin.readline().rstrip().split(' '))
    arr = []
    for y in range(3):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    time = 0
    find_flag = False

    while time < 101 :
        length_col = len(arr[0])
        length_row = len(arr)
        if len(arr) < target_y or len(arr[0]) < target_x :
            if length_row >= length_col :
                r_sort(arr)
            else:
                c_sort(arr)
            time +=1         
            continue
        if len(arr) > 100 :
            arr = arr[:100]
        if len(arr[0]) > 100 :
            for y in range(len(arr)):
                arr[y] = arr[y][:100]
        if arr[target_y-1][target_x-1] == target :
            find_flag = True
            break
        if length_row >= length_col :
            r_sort(arr)
        else:
            c_sort(arr)
        
        time += 1
    if not find_flag :
        time = -1
    print(time)
          
