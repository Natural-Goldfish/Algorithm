import sys
from collections import Counter

N = int(str.strip(sys.stdin.readline()))
counter = Counter(list(map(int, str.strip(sys.stdin.readline()).split(' '))))
M = int(str.strip(sys.stdin.readline()))

answer_list = []
for number in list(map(int, str.strip(sys.stdin.readline()).split(' '))):
    answer_list.append(counter[number])
print(' '.join(list(map(str, answer_list))))