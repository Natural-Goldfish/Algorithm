import sys

N = int(str.rstrip(sys.stdin.readline(), ''))
numbers = [int(str.rstrip(sys.stdin.readline(), '')) for _ in range(N)]
numbers.sort()
for number in numbers :
    print(number)
