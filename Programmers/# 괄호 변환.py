def step2(string):
    o, e, temp_index = 0, 0, 0
    
    for index, char in enumerate(string):
        if char == '(' :
            o += 1
        else : e += 1
        if o == e :
            temp_index = index
            break
    u, v = string[:temp_index+1], string[temp_index+1:]
    if check_string(u) :
        if len(v) != 0 : 
            v = step2(v)
        else : 
            return u
        return u + v
    else :
        if len(v) != 0 :
            v = step2(v)
        result = "(" + v + ")" + reverse_string(u[1:-1])
        return result
        
def check_string(string):
    if string[0]=='(':return True
    else : return False

def reverse_string(string):
    temp_string = ""
    if len(string) == 2 : return "()"
    for char in string:
        if char == '(':
            temp_string += ')'
        else :
            temp_string += '('
    return temp_string

def solution(p):
    answer = step2(p)
    print(answer)
    return answer