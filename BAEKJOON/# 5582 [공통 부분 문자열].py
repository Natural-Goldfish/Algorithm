import sys

s1 = str.strip(sys.stdin.readline())
s2 = str.strip(sys.stdin.readline())

table = list(list(0 for _ in range(len(s1)+1)) for _ in range(len(s2)+1))
answer = 0
for i in range(1, len(s2)+1):
    for k in range(1, len(s1)+1):
        if s2[i-1] == s1[k-1] :
            table[i][k] = table[i-1][k-1] + 1
            answer = max(answer, table[i][k])
print(answer)

