from collections import deque

n, k = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)
moved = [0] * (MAX + 1)

def track(s, f):
    route = []
    destination = k
    route.append(k)

    while destination != s:
        route.append(moved[destination])
        destination = moved[destination]

    route.reverse()

    print(' '.join(map(str, route)))

def bfs():
    q = deque([n])
    while q:
        x = q.popleft()

        if x == k:
            print(dist[x])
            track(n, k)
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                moved[nx] = x # 이전 정점이 무엇이었는지 기록
                q.append(nx)

bfs()