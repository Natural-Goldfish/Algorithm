import sys
from itertools import combinations

TEST_CASE = int(str.strip(sys.stdin.readline()))
answer_list = []
for test_case in range(1, TEST_CASE+1):
    N = int(str.strip(sys.stdin.readline()))

    fashion_dict = {}
    for n in range(N):
        item, category = str.strip(sys.stdin.readline()).split(' ')

        if category in fashion_dict :
            fashion_dict[category] += 1
        else :
            fashion_dict[category] = 2
    

    combination_num = None
    for key, item_num in fashion_dict.items():
        if combination_num == None :
            combination_num = 1
        combination_num *= item_num
    if combination_num == None :
        answer_list.append(0)
    else :
        answer_list.append(combination_num-1)

for answer in answer_list:
    print(answer)