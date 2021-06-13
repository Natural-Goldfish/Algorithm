def solution(absolutes, signs):
    return sum(absolutes[index] if signs[index] else -absolutes[index] for index in range(len(absolutes)))