def solution(n, results):
    n_dict = {number+1 : [set([]), set([])] for number in range(n)}
    for result in results:
        winner, loser = result
        
        n_dict[winner][1].add(loser)
        for player in n_dict[loser][1]:
            n_dict[winner][1].add(player)
            n_dict[winner][1] |= n_dict[player][1]
            n_dict[player][0].add(winner)
            n_dict[player][0] |= n_dict[winner][0]
            
        n_dict[loser][0].add(winner)
        for player in n_dict[winner][0]:
            n_dict[loser][0].add(player)
            n_dict[loser][0] |= n_dict[player][0]
            n_dict[player][1].add(loser)
            n_dict[player][1] |= n_dict[loser][1]
    answer = 0
    for key, item in n_dict.items():
        if len(item[0]) + len(item[1]) + 1 == n :
            answer += 1
    return answer