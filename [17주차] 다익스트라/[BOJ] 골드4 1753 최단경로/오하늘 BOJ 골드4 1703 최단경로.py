import sys
input = sys.stdin.readline
import heapq
INF = (1e9) # 무한대

v, e = map(int, input().split()) # 정점, 간선
k = int(input()) # 시작
g = [[] for i in range(v+1)] # 그래프 즉 간선 + 1
distance = [INF] * (v+1) # 최단거리 테이블
visited = [False] * (v+1)

for _ in range(e): # 거리 정수 추가
    u, v, w = map(int, input().split())
    g[u].append((v,w))

def dijkstra(start):
    q = [] # q는 (거리, 갈 정점)
    heapq.heappush(q, (0,start)) # 처음이니 0
    distance[start] = 0
    visited[start] = True

    while q:
        dist, now = heapq.heappop(q) # 가중치, 현재 정점

        for i in g[now]:
            cost = dist + i[1] # 현재의 가중치 + 다음정점까지의 가중치

            if cost < distance[i[0]]: # 비용이 그다음 정점의 최단거리테이블보다 작을때
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                visited[i[0]] = True


dijkstra(k)
for i in range(1,len(distance)):
    if i == 0 : continue
    if distance[i] == 1e9:
        print('INF')
    else:
        print(distance[i])