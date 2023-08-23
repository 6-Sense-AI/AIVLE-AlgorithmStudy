# 사알짝 건드려만봄..
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력받기
# 방문확인을 위한 visited 만들기
n, m, x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

# 양방향으로 연결
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))



def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    visited[start] = True
    
    while q:
        dist, now = heapq.heappop(q)