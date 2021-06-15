import sys

N = int(str.rstrip(sys.stdin.readline(), ''))
times = sorted(list(map(int, str.rstrip(sys.stdin.readline(), '').split(' '))))
for index, item in enumerate(times[1:]):
    times[index+1] = times[index] + item
print(sum(times))


    
