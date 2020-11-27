class BAEKJOON:
    def solution(self, stairNum, points):
        self.array = [points[0]]
        if stairNum == 1 : return self.array.pop()
        self.array.append(max(points[0] + points[1], points[1]))
        if stairNum == 2 : return self.array.pop()
        self.array.append(max(points[0] + points[2], points[1] + points[2]))
        if stairNum == 3 : return self.array.pop()

        for i in range(3, stairNum):
            self.array.append(max(self.array[i - 3] + points[i] + points[i - 1], self.array[i - 2] + points[i]))
        return self.array.pop()            

if __name__ == "__main__":
    stairNum = int(input())
    points = []
    for i in range(stairNum):
        points.append(int(input()))

    baekjoon = BAEKJOON()
    print(baekjoon.solution(stairNum, points))