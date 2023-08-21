

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

## 지름길 개수, 고속도로 길이 입력

n , d = map(int,input().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


## 기본 거리 1

for i in range(d):
    graph[i].append((i+1, 1))


for _ in range(n):
    s, e, l = map(int,input().split())

    ## 고속도로 외부 지점은 필요없음
    if e > d:  
        continue
    graph[s].append((e,l))

dijkstra(0)
print(distance[d])
 