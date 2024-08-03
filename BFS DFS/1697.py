"""
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
"""
"""
# 1697번 : 숨바꼭질
from collections import deque

def bfs():
    q = deque()             # deque는 양쪽에서 입출력 가능
    q.append(n)             # q = deque([5])
    while  q:
        x = q.popleft()     # 처음 시작점은 x = 5, q = deque([])
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2):    # nx = 4, 6, 10
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)    # q = deque([4, 6, "10"])

MAX = 10 ** 5               # 시간초과 안나게 수 제한
dist = [0] * (MAX + 1)      # 이동하는 거리를 알기 위한 변수
n, k = map(int, input().split())

bfs()

"""
## 다시 풀어보기
