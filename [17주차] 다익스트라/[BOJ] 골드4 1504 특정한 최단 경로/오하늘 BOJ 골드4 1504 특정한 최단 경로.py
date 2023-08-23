# 반례도 다 돌려봤는데 왜 틀렸는지 모르겠음..

import sys
input = sys.stdin.readline
INF = int(1e9)

import heapq

n, e = map(int, input().split()) # 정점, 간선

g = [[] for i in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

for i in range(e): # 양방향
    a,b,c = map(int, input().split())
    g[a].append((b,c))
    g[b].append((a,c))

v1, v2 = map(int, input().split()) # 정점 1

# 다익스트라 함수
def dijkstra(start, flag):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    visited[start] = True

    while q:
        dist, now = heapq.heappop(q) # 거리, 현재

        if flag == 1 and now > v1: # 정점1 넘으면
            continue

        if flag ==2 and now > v2:
            continue
        
        for i in g[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                visited[i[0]] = True

#case 1
dijkstra(1,1)
ans1 = distance[v1]

distance = [INF] * (n+1)
visited = [False] * (n+1)
dijkstra(v1,2)
ans2 = distance[v2]

distance = [INF] * (n+1)
visited = [False] * (n+1)
dijkstra(v2,3)
ans3 = distance[n]

result1 = ans1+ans2+ans3

#case 2
distance = [INF] * (n+1)
visited = [False] * (n+1)
dijkstra(1,1)
ans1 = distance[v2]

distance = [INF] * (n+1)
visited = [False] * (n+1)
dijkstra(v2,2)
ans2 = distance[v1]

distance = [INF] * (n+1)
visited = [False] * (n+1)
dijkstra(v1,3)
ans3 = distance[n]

result2 = ans1+ans2+ans3

if result1>result2:
    print(result2)
else: print(result1)