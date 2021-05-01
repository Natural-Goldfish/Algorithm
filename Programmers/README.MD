# 수식 최대화 | PROGRAMMERS
### Solution
---
1. 숫자와 수식 분리
2. 우선 순위를 정하기 위해 가능한 순열 구함
3. 연산은 숫자의 index와 index+1이 연산되는 결과이다. 따라서 우선순위에 일치하는 수식이라면 index를 None으로 변환 후, 계속해서 연산 진행
4. 최대값 갱신

</br></br>

# 메뉴 리뉴얼 | PROGRAMMERS
### Solution
---
1. 가능한 조합 순회
2. 같은 길이의 조합의 경우에는, 최대 빈도수를 가지는 조합만 등록

</br></br>

# 괄호 변환 | PROGRAMMERS
### Solution
---
1. 조건에 따라 구현
</br></br>

# 뉴스 클러스터링 | PROGRAMMERS
### Solution
---
1. 교집합은 작은 수, 합집합은 큰 수 선택
</br>

### Plus
---
- **정규식**
    </br>  

    1. sub(문자열 대체)
        > re.sub({target pattern}, {replaced string}, {target string})
    </br>

    ```
    >>> import re
    >>> string = "AbcdE)_v"
    >>> new_string = re.sub(r'[^a-z]', "", string)
    >>> print(new_string)
    bcdv
    ```   
</br></br>

# 영어 끝말잇기 | PROGRAMMERS
### Solution
---
1. 다음 단어는 이전 단어의 끝 문자로 시작해야 한다.
</br>

### Plus
---
- **str.startswith()**
    </br>

    ```
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

# 오픈 채팅방 | PROGRAMMERS
### Solution
---
1. user id의 변화 파악을 위해 dict에서 관리
2. 출입 정보 리스트에 저장
3. 출력
</br></br>

# [1차] 캐시 | PROGRAMMERS
### Solution
---
1. LRU(Least Recently Used)를 위해 deque사용
</br>

### Plus
---
- **deque 삭제**
    </br>

    1. Element 기반 삭제
        > deque.remove(INSTANCE, ELEMENT)
    </br>

    2. Index 기반 삭제
        > del INSTANCE[INDEX]
    </br>

    ```
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

# [1차] 프렌즈 4블록 | PROGRAMMERS
### Solution
---
1. 현재 블록, 우측 블록, 아래 블록, 우하단 블록이 일치하는지 검사
2. 이미 기존에 부숴지는 것으로 예정된 값을 제외하고, 새롭게 부숴지는 블록의 값을 더한다.
3. 그냥 단순 코딩
</br></br>

# 점프와 순간 이동 | PROGRAMMERS
### Solution
---
1. 2로 나누어 떨어지지 않으면 -1, 비용 +1
</br></br>


