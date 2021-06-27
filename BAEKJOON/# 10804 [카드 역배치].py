import sys

cards = list(number for number in range(1, 21))
for _ in range(10):
    a, b = map(int, str.rstrip(sys.stdin.readline(), '').split(' '))
    temp = cards[a-1 : b]
    temp.reverse()
    cards[a-1 : b] = temp
print(" ".join(map(str, cards)))
    
