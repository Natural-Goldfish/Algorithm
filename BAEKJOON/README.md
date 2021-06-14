# 2357 [최솟값과 최댓값](https://www.acmicpc.net/problem/2357)
## Solution

주어진 구간마다 배열을 정렬한 뒤 최소값과 최대값을 찾게 되면, 최악의 경우 N^2의 시간이 소요됩니다. 따라서, 일정 범위에 대한 정보 값을 logn 으로 얻을 수 있는 _segment tree_ 를 이용하여 해결했습니다.  
[참고 링크](https://www.acmicpc.net/blog/view/9)

</br></br>

---

# 2750 [수 정렬하기](https://www.acmicpc.net/problem/2750)
## Solution

단순하게 숫자를 정렬합니다.

</br></br>

---

# 2085 [나무자르기](https://www.acmicpc.net/problem/2805)
## Solution

자르는 높이의 범위를 반씩 줄여나가는 이분 탐색을 사용합니다.

</br></br>

---

# 1712 [손익분기점](https://www.acmicpc.net/problem/1712)
## Solution

수식을 _판매 이익 X 판매 개수 > 고정 비용 + 가변 비용 X 판매 개수_ 로 정의하고, 참이 되는 _판매 개수_ 를 구합니다. 판매 이익과 가변 비용이 같은 경우에는 손익분기점이 생길 수 없으므로, 해당 부분을 예외 처리합니다.

</br></br>

---

# 1927 [최소 힙](https://www.acmicpc.net/problem/1927)
## Solution

Python heapq module을 사용하면 단순한 구현 문제로 해결 할 수 있습니다.

</br></br>

---

# 1920 [수 찾기](https://www.acmicpc.net/problem/1920)
## Solution

이진 탐색 트리를 사용합니다.

</br></br>

---