
def solution(N):
    Three = 3
    Five = 5
    maxNum = int(N / Five)
    while(maxNum != -1):
        less = N - maxNum*Five
        if less % Three == 0: 
            print(int(less/Three) + maxNum)
            break
        else : maxNum -= 1
    if maxNum == -1 : print(-1)


if __name__ == "__main__":
    N = int(input())
    solution(N)