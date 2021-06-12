class BAEKJOON:
    def solution(self, n):
        self.array = [0] * (n+1)
        
        if n == 1 :
            return 0
        else :
            for i in range(2, n + 1):
                self.array[i] = self.array[i - 1] + 1
                if i % 2 == 0 and self.array[i//2] + 1 < self.array[i] :
                    self.array[i] = self.array[i//2] + 1
                if i % 3 == 0 and self.array[i//3] + 1 < self.array[i] :
                    self.array[i] = self.array[i//3] + 1
            return self.array[n]
if __name__ == "__main__":
    baekjoon = BAEKJOON()
    print(baekjoon.solution(int(input())))