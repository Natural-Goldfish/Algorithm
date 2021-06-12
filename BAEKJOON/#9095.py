class BAEKJOON:

    def solution(self, n):
        self.array = [0, 1, 2, 4]
        if n == 1 : return 1
        elif n == 2 : return 2
        elif n == 3 : return 4
        else :
            for i in range(4, n + 1) :
                self.array.append(self.array[i - 1] + self.array[i - 2] + self.array[i - 3])
            return self.array[n]
if __name__ == "__main__":
    testCase = int(input())
    testInput = []
    for i in range(testCase):
        testInput.append(int(input()))
    for i in range(testCase):
        print(BAEKJOON().solution(testInput[i]))

