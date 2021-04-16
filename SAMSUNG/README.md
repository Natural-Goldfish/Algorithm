# 5658. [모의 SW 역량테스트] 보물상자 비밀번호
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