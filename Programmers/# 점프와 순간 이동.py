def solution(n):
    time = 1
    while n != 1 :
        if n%2 != 0 :
            time += 1
        n = int(n/2)
    return time