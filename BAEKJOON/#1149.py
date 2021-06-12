class BAEKJOON:
    def solution(self, n, costList):
        self.array = [[0]*(n+1), [0]*(n+1), [0]*(n+1)]
        self.array[0][1] = costList[0][0]
        self.array[1][1] = costList[0][1]
        self.array[2][1] = costList[0][2]

        for i in range(2, n + 1):
            self.array[0][i] = min(self.array[1][i-1], self.array[2][i-1]) + costList[i - 1][0]
            self.array[1][i] = min(self.array[0][i-1], self.array[2][i-1]) + costList[i - 1][1]
            self.array[2][i] = min(self.array[0][i-1], self.array[1][i-1]) + costList[i - 1][2]
        costs = []
        for i in range(3):
            costs.append(self.array[i][n])
        return(min(costs))
if __name__ == "__main__":
    houseNum = int(input())
    houseColor = []
    for i in range(houseNum):
        houseColor.append(list(map(int, input().split(" "))))

    baekjoon = BAEKJOON()
    print(baekjoon.solution(houseNum, houseColor))