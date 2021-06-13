# 음양 더하기
## Solution

단순 덧셈 문제입니다.

</br></br>

---

# 게임 맵 최단거리 | PROGRAMMERS
## Solution

1. BFS

</br></br>

---

# 수식 최대화 | PROGRAMMERS
## Solution

1. 숫자와 수식 분리
2. 우선 순위를 정하기 위해 가능한 순열 구함
3. 연산은 숫자의 index와 index+1이 연산되는 결과이다. 따라서 우선순위에 일치하는 수식이라면 index를 None으로 변환 후, 계속해서 연산 진행
4. 최대값 갱신

</br></br>

---

# 메뉴 리뉴얼 | PROGRAMMERS
## Solution

1. 가능한 조합 순회
2. 같은 길이의 조합의 경우에는, 최대 빈도수를 가지는 조합만 등록

</br></br>

---

# 괄호 변환 | PROGRAMMERS
## Solution

1. 조건에 따라 구현

</br></br>

---

# 뉴스 클러스터링 | PROGRAMMERS
## Solution

1. 교집합은 작은 수, 합집합은 큰 수 선택

</br>

## 정규식

- sub(문자열 대체)
    
    > re.sub({target pattern}, {replaced string}, {target string})

    </br>

    ```python
    >>> import re
    >>> string = "AbcdE)_v"
    >>> new_string = re.sub(r'[^a-z]', "", string)
    >>> print(new_string)
    bcdv
    ```   
    
</br></br>

---

# 영어 끝말잇기 | PROGRAMMERS
## Solution

1. 다음 단어는 이전 단어의 끝 문자로 시작해야 한다.

</br>

## 문자열

- str.startswith()

    </br>

    ```python
    >>> string = 'abcde'
    >>> string.startswith('ab')
    True
    >>> string.startswith('a')
    True
    >>> str.startswith(string, 'a')
    True
    >>> string.startswith('d')
    False
    ```
    
</br></br>

---

# 오픈 채팅방 | PROGRAMMERS
## Solution

1. user id의 변화 파악을 위해 dict에서 관리
2. 출입 정보 리스트에 저장
3. 출력

</br></br>

---

# [1차] 캐시 | PROGRAMMERS
## Solution

1. LRU(Least Recently Used)를 위해 deque사용

</br>

## deque

- Element 기반 삭제
    > deque.remove(INSTANCE, ELEMENT)

- Index 기반 삭제
    > del INSTANCE[INDEX]
    
    </br>

    ```python
    >>> from collection import deque
    >>> a = deque([1, 2, 3, 4])
    >>> a.remove(1)
    >>> a
    deque([2, 3, 4])
    >>> del a[2]
    >>> a
    deque([2, 3])
    ```
    
</br></br>

---

# [1차] 프렌즈 4블록 | PROGRAMMERS
## Solution

1. 현재 블록, 우측 블록, 아래 블록, 우하단 블록이 일치하는지 검사
2. 이미 기존에 부숴지는 것으로 예정된 값을 제외하고, 새롭게 부숴지는 블록의 값을 더한다.
3. 그냥 단순 코딩

</br></br>

---

# 점프와 순간 이동 | PROGRAMMERS
## Solution

1. 2로 나누어 떨어지지 않으면 -1, 비용 +1

</br></br>

---

# 조이스틱 | PROGRAMMERS
## Solution

1. 정방향으로 가는 거리와, 뒤로 이동하여 접근하는 거리의 최소값 비교
2. 목표 문자까지 A부터 올라가는 횟수와, Z부터 내려가는 횟수의 최소값 비교

</br></br>

---

# 순위 | PROGRAMMERS
## Solution

1. 전체 갱신하는 방법
2. 다시 생각해보기

</br></br>

---

# 1922. 네트워크 연결 | BAEKJOON
## Solution

1. 크루스칼 알고리즘 사용
2. 연결 그래프를 확인하는 방법으로 서로소 집합을 활용

</br></br>

---

