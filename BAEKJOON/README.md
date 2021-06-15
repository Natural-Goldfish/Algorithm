# 11286 [절대값 힙](https://www.acmicpc.net/problem/11286)
## Solution

Python _heapq module_ 을 사용하면 쉽게 해결할 수 있습니다. Python _heapq module_ 에 (item<sub>0</sub>, item<sub>1</sub>, .. , item<sub>n-1</sub>, item<sub>n</sub>) 을 push했을 때, item<sub>0</sub>를 비교 대상으로 설정합니다.


# 11279 [최대 힙](https://www.acmicpc.net/problem/11279)
## Solution

Python _heapq module_ 을 사용하면 쉽게 해결할 수 있습니다. Python _heapq module_ 은 기본 설정으로 min heap을 구성하기 때문에, 음수 값을 push하는 것으로 max heap과 같은 역할을 수행하도록 할 수 있습니다.

</br></br>

---

# 7569 [토마토](https://www.acmicpc.net/problem/7569)
## Solution

2차원 배열이 아닌 3차원 배열을 이용해야 했으며, c층의 익은 토마토를 기준으로 c-1, c+1층의 동일한 w, h를 가지는 토마토만 영향을 받는것에 주의해야합니다. 영향을 받는 토마토를 탐색하기 위해 _BFS(너비 우선 탐색)_ 을 사용했습니다.

</br></br>

---

# 1916 [최소비용 구하기](https://www.acmicpc.net/problem/1916)
## Solution

모두 양의 가중치를 가지고 있는 그래프에서, 임의의 정점 P<sub>i</sub>에서 다른 정점 P<sub>j</sub>까지의 최소 비용을 구하기 위해 _dijkstra(다익스트라)_ 를 사용했습니다. 

</br></br>

---

# 11403 [경로 찾기](https://www.acmicpc.net/problem/11403)
## Solution

가중치가 없는 방향 그래프에서 정점 P<sub>i</sub>에서 다른 정점 P<sub>j</sub>로 가는 경로가 있는지 검사하기 위해, _BFS(너비 우선 탐색)_ 을 이용하여 문제를 해결했습니다.

</br></br>

---

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

자르는 높이의 범위를 반씩 줄여나가는 _Binary search(이분 탐색)_ 을 사용했습니다.

</br></br>

---

# 1712 [손익분기점](https://www.acmicpc.net/problem/1712)
## Solution

수식을 _판매 이익 X 판매 개수 > 고정 비용 + 가변 비용 X 판매 개수_ 로 정의하고, 참이 되는 _판매 개수_ 를 구합니다. 판매 이익과 가변 비용이 같은 경우에는 손익분기점이 생길 수 없으므로, 해당 부분을 예외 처리합니다.

</br></br>

---

# 1927 [최소 힙](https://www.acmicpc.net/problem/1927)
## Solution

Python _heapq module_ 을 사용하여 단순한 구현 문제로 해결했습니다.

</br></br>

---

# 1920 [수 찾기](https://www.acmicpc.net/problem/1920)
## Solution

_Binary search tree(이진 탐색 트리)_ 를 사용했습니다.

</br></br>

---