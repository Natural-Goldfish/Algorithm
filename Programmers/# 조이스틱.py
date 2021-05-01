def finder(name, cur_index, visited):
    target_indexA = 0
    for index in range(cur_index, len(name)):
        if name[index] != 'A' and index not in visited:
            target_indexA = index
            break
    target_indexB = 0            
    for index in range(len(name)-1, -1, -1):
        if name[index] != 'A' and index not in visited:
            target_indexB = index
            break
    return target_indexA-cur_index, cur_index+len(name)-target_indexB
        
def solution(name):
    change_num = len(list(filter(lambda x : x != 'A', name)))
    if change_num == 0 : return 0
    
    move, changed, flag, visited = 0, 0, False, set([])
    cur_index = 0
    while changed != change_num :
        front, back = finder(name, cur_index, visited)
        if back < front :
            move = move + cur_index + 1
            flag = True
            break
        cur_index, move = cur_index + front, move + front
        visited.add(cur_index)
        move += min(ord(name[cur_index])-ord('A'), ord('Z')-ord(name[cur_index])+1)
        changed += 1
    if flag :
        for cur_index in range(len(name)-1, -1, -1):
            if name[cur_index] == 'A':
                move += 1
                continue
            move += min(ord(name[cur_index])-ord('A'), ord('Z')-ord(name[cur_index])+1)
            changed += 1 
            if changed == change_num : break
            move += 1
    return move