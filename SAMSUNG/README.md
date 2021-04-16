# 5658. [모의 SW 역량테스트] 보물상자 비밀번호
### Solution
---
1. N//4번 회전하면 동일한 숫자가 구성되므로, N//4-1만큼 rotation.
2. N//4개씩 잘라서 set에 저장(Unique)
3. 오름차순 정렬
4. 진법 변환

### Plus
---
- **Python deque는 sequence type으로 slice가 안되는 것에 주의할 것.**
```
>>> temp = deque([1, 2, 3, 4])
>>> temp[0 : 2]
TypeError: sequence index must be integer, not 'slice'
```
- **n진법으로 표현가능한 문자열 s는 int(s, n)을 사용하면, n진법으로 계산된 값이 반환된다.**
```
>>> int('201', 3)
19
>>> int('1F7', 16)
503
```

# 5656. [모의 SW 역량테스트] 벽돌 깨기
### Solution
---
1. 모든 케이스 검사(중복 순열)
2. 각 케이스 마다, BFS 수행
3. 벽돌 깨지고 나면, 그래프 갱신(해당 부분 수정으로 시간 통과)
4. 가장 많이 벽돌을 깬 케이스를 찾기 위해서, BFS수행 할때 count 측정

### Plus
---
- **input() 문자열 처리시, rstrip()으로 개행 문자 없앨 것**
- **중복 순열 사용 방법**
```
from itertools import product
product([1, 2, 3], repeat=n)    # n개 반복 허용
```