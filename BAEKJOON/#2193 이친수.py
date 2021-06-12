def solution(N):
    if N == 1 : 
        print(1)
    elif N == 2 : 
        print(1)
    else :
        back2 = 1 
        back1 = 1
        curValue = 1
        for i in range(3, N + 1):
            curValue = back2 + back1
            back2 = back1
            back1 = curValue
        print(curValue)

if __name__ == "__main__":
    N = int(input())
    solution(N)