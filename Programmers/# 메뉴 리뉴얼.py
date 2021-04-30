from itertools import combinations
def solution(orders, course):
    menu_list = []
    for order in orders:
        menu_list.append(list(map(lambda x : x, order)))
    
    course_max = {length : 0 for length in course}
    menu_dict = {length : [] for length in course}
    for combination_length in course:
        for index in range(len(menu_list)):
            possible_cases = combinations(menu_list[index], combination_length)
            for possible_case in possible_cases:
                possible_case = sorted(possible_case)
                if "".join(possible_case) in menu_dict[combination_length] : continue
                count = 0
                for index2 in range(len(menu_list)):
                    if index == index2 : continue
                    possible_cases2 = combinations(menu_list[index2], combination_length)
                    possible_cases2 = map(lambda x : sorted(x), possible_cases2)
                    if possible_case in possible_cases2 :
                        count += 1
                if count == 0 : continue
                if count == course_max[combination_length] : 
                    menu_dict[combination_length].append("".join(possible_case))
                elif count > course_max[combination_length]:
                    menu_dict[combination_length] = ["".join(possible_case)]
                    course_max[combination_length] = count
    print(menu_dict)
    return []