import sys, copy
from collections import deque 

N, M = map(int, str.strip(sys.stdin.readline()).split(' '))
student_dict = {student : {'taller' : set([]), 'smaller' : set([])} for student in range(1, N+1)}

for m in range(M):
    student1, student2 = map(int, str.strip(sys.stdin.readline()).split(' '))
    student_dict[student1]['taller'].add(student2)
    student_dict[student2]['smaller'].add(student1)
answer = 0
def bfs(start, student_dict):
    global answer, N
    queue = deque([('start', start)])
    visited = set([])
    count = 1
    while queue :
        
        keyword, cur_student = queue.popleft()
        if cur_student in visited : continue
        visited.add(cur_student)
        t_flag, s_flag = False, False

        if keyword == 'start' :
            t_flag = True
            s_flag = True
        elif keyword == 'taller' :
            t_flag = True
            count += 1
        elif keyword == 'smaller' :
            s_flag = True
            count += 1

        if t_flag :
            for student in student_dict[cur_student]['taller'] :
                queue.append(('taller', student))
        if s_flag :
            for student in student_dict[cur_student]['smaller'] :
                queue.append(('smaller', student))
    if count == N :
        answer += 1


for student in range(1, N+1):
    bfs(student, student_dict)
print(answer)

