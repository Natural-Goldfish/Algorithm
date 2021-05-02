# def find(parent, element):
#     if parent[element] == element :
#         return element
#     parent[element] = find(parent, parent[element])
#     return parent[element]

# def union(parent, u, v):
#     u = find(parent, u)
#     v = find(parent, v)
#     if (u == v) : return False
#     parent[v] = u
#     return True
if __name__ == "__main__":
    N = int(input().rstrip())
    M = int(input().rstrip())
    costs = []
    computer_set = [set([index]) for index in range(N)]

    for m in range(M):
        comA, comB, cost = map(int, input().rstrip().split(' '))
        costs.append((comA-1, comB-1, cost))
    costs.sort(key=lambda x : x[2])
    answer = 0
    for item in costs:
        comA, comB, cost = item
        if not computer_set[comA].isdisjoint(computer_set[comB]) : continue

        if len(computer_set[comA]) >= len(computer_set[comB]) :
            temp_set = computer_set[comB] - computer_set[comA]
            for item in temp_set :
                computer_set[comA].add(item)
            for item in temp_set:
                computer_set[item] = computer_set[comA]
            computer_set[comB] = computer_set[comA]
        else :
            temp_set = computer_set[comA] - computer_set[comB]
            for item in temp_set :
                computer_set[comB].add(item)
            for item in temp_set :
                computer_set[item] = computer_set[comB]
            computer_set[comA] = computer_set[comB]
        answer += cost
    print(answer)