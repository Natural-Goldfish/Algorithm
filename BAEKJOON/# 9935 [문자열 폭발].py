import sys
from collections import deque

s = deque(map(str, str.strip(sys.stdin.readline())))
boom = deque(map(str, str.strip(sys.stdin.readline())))

lps = list(0 for _ in range(len(boom)))
si = 1
pi = 0
while (si < len(boom) and pi < len(boom)) :
    if boom[si] == boom[pi] :
        lps[si] = lps[si-1] + 1
        si += 1
        pi += 1
    else :
        lps[si] = lps[lps[si-1]]
        pi = lps[si]
        if pi == 0 :
            si += 1

si = 0
pi = 0
p = boom
answer = deque([])

while (s and si < len(s)) :
    if s[0] == p[pi] :
        pi += 1
        answer.append(s.popleft())

        if pi == len(p):
            lp = len(p)
            while(lp):
                answer.pop()
                lp -=1 
            lp = len(p)
            while(lp):
                if not answer : break
                s.appendleft(answer.pop())
                lp -= 1
            pi = 0

    else :
        if pi == 0 :
            answer.append(s.popleft())
            continue
        if lps[pi-1] == 0 :
            pi = 0
        else :
            pi = lps[lps[pi-1]]

if answer :
    print(''.join(list(answer)))
else :
    print("FRULA")