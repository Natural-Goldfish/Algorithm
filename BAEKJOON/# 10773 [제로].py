import sys

K = int(str.strip(sys.stdin.readline()))
answer_list = []
for k in range(K):
    number = int(str.strip(sys.stdin.readline()))
    answer_list.append(number) if number else answer_list.pop()
print(sum(answer_list))