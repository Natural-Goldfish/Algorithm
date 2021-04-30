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
- **정규식 표현 sub**
</br>  

> re.sub({target pattern}, {replaced string}, {target string})
</br>

```
>>> import re
>>> string = "AbcdE)_v"
>>> new_string = re.sub(r'[^a-z]', "", string)
>>> print(new_string)
bcdv
```   

