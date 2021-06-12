class BAEKJOON:
    def solution(self, n):
        self.array = [0, 1, 2]

        if n == 1 : return 1
        if n == 2 : return 2
        else :
            for i in range(3, n + 1):
                self.array.append(self.array[i - 1] + self.array[i - 2])
            return self.array[n]

if __name__ == "__main__":
    N = int(input())
    baekjoon = BAEKJOON()
    print(baekjoon.solution(N))
