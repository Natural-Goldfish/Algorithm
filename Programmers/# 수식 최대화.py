from itertools import permutations
import copy

def solution(expression):
    answer = -1
    numbers, expression_list = expression, []
    for char in ['+', '*', '-']:
        numbers = numbers.replace(char, " ")
    numbers = list(map(int, numbers.split(" ")))
    
    for express in expression:
        if express == '+' or express=='-' or express == '*':
            expression_list.append(express)
    possible_cases = permutations(list(set(expression_list)), len(set(expression_list)))
    
    for possible_case in possible_cases:
        temp_numbers = copy.deepcopy(numbers)
        temp_expressions = copy.deepcopy(expression_list)
        for priority in possible_case :
            for index, formula in enumerate(temp_expressions):
                if formula == priority :
                    if priority == '+' :
                        temp_numbers[index+1] = temp_numbers[index] + temp_numbers[index+1]
                        temp_numbers[index] = None
                    elif priority == '-':
                        temp_numbers[index+1] = temp_numbers[index] - temp_numbers[index+1]
                        temp_numbers[index] = None
                    else :
                        temp_numbers[index+1] = temp_numbers[index] * temp_numbers[index+1]
                        temp_numbers[index] = None
            temp_numbers = list(filter(lambda x : x != None, temp_numbers))
            temp_expressions = list(filter(lambda x : x != priority, temp_expressions))
        result = temp_numbers[0]
        if result < 0 :
            result = abs(result)
        answer = max(answer, result)
    return answer