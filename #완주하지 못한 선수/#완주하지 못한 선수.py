def solution(participant, completion):
    answer = ''
    started = {}
    for i in range(len(participant)):
        if participant[i] in started.keys() :
            started[participant[i]] += 1
        else :
            started[participant[i]] = 1
    
    for i in range(len(completion)):
        if completion[i] in started.keys():
            started[completion[i]] -= 1
    
    for key, value in started.items():
        if value > 0 :
            answer = key
    
    return answer

    