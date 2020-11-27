class BAEKJOON:
    def solution(self, n):
        self.zero = [1, 0]
        self.one = [0, 1]
        if n == 0 : return 1, 0
        if n == 1 : return 0, 1
        for i in range(2, n + 1):
            self.zero.append(self.zero[i - 2] + self.zero[i - 1])
            self.one.append(self.one[i - 2] + self.one[i - 1])
        return self.zero[n], self.one[n]

if __name__ == "__main__":
    testCase = int(input())
    baekjoon = BAEKJOON()
    testInput = []
    for i in range(testCase):
        testInput.append(int(input()))
    
    for testNumber in testInput:
        zero, one = baekjoon.solution(testNumber)
        print(zero, end = " ")
        print(one)


    
    