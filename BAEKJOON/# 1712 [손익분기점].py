import sys
cost1, cost2, cost3 = map(int, str.rstrip(sys.stdin.readline(), '').split(' '))
if cost3 == cost2 :
    print(-1)
else :
    if cost1/(cost3-cost2) < 0 : print(-1)
    else : print(int(cost1/(cost3-cost2))+1)
