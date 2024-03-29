import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

# 입력받기
n, d = map(int, input().split())

graph = [[] for i in range(d + 1)]
distance = [INF] * (d + 1)

# 모든 거리 1로 설정
for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    graph[a].append((b, c))

# 다익스트라
def fastLoad(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


fastLoad(0)
print(distance[d])