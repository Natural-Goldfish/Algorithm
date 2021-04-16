T = int(input()) # TEST CASE
N, K = map(int, input().split(" "))

def add_unique(numbers, unique_num, jump):
    for index in range(0, len(numbers), jump):
        unique_num.add("".join(numbers[index : index + jump]))

for test_case in range(1, T+1):
    numbers = [char for char in input()]
    jump = N//4
    unique_num = set()

    for i in range(0, jump):
        add_unique(numbers, unique_num, jump)
        numbers = [numbers.pop()] + numbers
    find_number = sorted(list(unique_num), reverse=True)[K-1]
    print(find_number)
    answer = int(find_number, 16)
    print(answer)