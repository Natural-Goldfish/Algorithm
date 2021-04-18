from itertools import permutations

if __name__ == "__main__":
    N = int(input().rstrip())
    numbers = list(map(int, input().rstrip().split(' ')))
    max_value, min_value = -1000000001, 1000000001
    temp_cal_format = []
    for index, fomula_num in enumerate(map(int, input().rstrip().split(' '))):
        if index == 0 :                                         # +
            temp_cal_format += ['+' for i in range(fomula_num)]
        elif index == 1 :                                       # -
            temp_cal_format += ['-' for i in range(fomula_num)]
        elif index == 2 :                                       # *
            temp_cal_format += ['*' for i in range(fomula_num)]
        elif index == 3 :                                       # /
            temp_cal_format += ['/' for i in range(fomula_num)]
    
    possible_cases = permutations(temp_cal_format)
    temp_cal_format = None
    
    for case in possible_cases :
        a = numbers[0]
        for index in range(1, len(numbers)):
            b, cal_format = numbers[index], case[index - 1]
            if cal_format == '+' :
                a += b
                continue
            elif cal_format == '-' :
                a -= b
                continue
            elif cal_format == '*' :
                a *= b
            elif cal_format == '/' :
                if a < 0 :
                    a = -(abs(a)//b)
                    continue
                else :
                    a //= b
                    continue
        
        max_value = max(a, max_value)
        min_value = min(a, min_value)
    print(max_value, '\n', min_value, sep="")

                
            
            
