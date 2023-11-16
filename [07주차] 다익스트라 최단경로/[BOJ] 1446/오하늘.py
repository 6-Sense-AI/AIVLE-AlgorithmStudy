#지름길 - 다익스트라
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #10억. 최대값

n, d = map(int, input().split()) # 지름길 개수, 고속도로 개수
graph = [[] for i in range(d+1)] # 지름길을 담는 그래프
distance = [INF]*(d+1) # distance를 무한이 아니라 그 수대로 넣어주어야 함

for i in range(d+1):
    distance[i] = i # 일단 모든 거리가 다 비용임

# 지름길 정보
for i in range(n):
    start, end, d_l = map(int, input().split()) # 시작, 도착, 지름길 길이
    graph[start].append((end,d_l))
    # if d_l < start-end:
    #     if d_l < distance[i]:
    #         distance[i] = d_l
    
def dijkstra(start): # 다익스트라 시작
    q = [] #최소 힙
    heapq.heappush(q, (0, start)) # 시작은 무조건 0
    distance[start] = 0 # 시작비용 0
    while q:
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보
        if distance[now] < dist: #거리, 정점
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1] # 0은 연결된 노드 ,1은 비용
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(0)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
        
