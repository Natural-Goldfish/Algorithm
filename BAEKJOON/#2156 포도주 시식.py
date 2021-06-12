def solution(N, List):
    if N == 1 : print(List[0])
    elif N == 2 : print(sum(List))
    elif N == 3 :
        print(max(List[0] + List[1], List[1] + List[2], List[0]+ List[2]))
    else :
        array = [List[0], List[0] + List[1], max(List[0] + List[2], List[1] + List[2], List[0] + List[1])]
        for i in range(3, len(List)):
            array.append(max(array[i - 3] + List[i - 1] + List[i], array[i - 2] + List[i], array[i - 1]))
        print(max(array))

if __name__ == "__main__":
    N = int(input())
    List = []
    for i in range(N):
        temp = int(input())
        List.append(temp)
    solution(N, List)
    