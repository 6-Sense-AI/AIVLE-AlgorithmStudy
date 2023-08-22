import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력받기
v, e = map(int, input().split())
k = int(input())
graph = [[] for i in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# 기본 다익스트라
def dijstra(start):
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

dijstra(k)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])