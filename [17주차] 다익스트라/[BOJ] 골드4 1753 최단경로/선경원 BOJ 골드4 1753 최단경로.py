

## 방향그래프가 주어지면 주어진 시작점에서 
## 다른 모든 정점으로의 최단 경로를 구하는 프로그램


## 처음에 ppt 있는 코드대로 했더니 자꾸 시간초과 나옴
## 최소값을 리턴해주는 Heap을 사용해보자


import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


## deque 쓰는 거랑 비슷함
## 꺼내와서 비교하고 갱신하고 추가하고

def dijkstra(start):
    distances = [float("inf")]*(V+1)
    distances[start] = 0
    q = []
    heapq.heappush(q, (distances[start], start))
    

    ## 현재까지 최소 거리와 노드를 꺼내와서 비교
    while q:
        cnt_distance, node = heapq.heappop(q)
        
        if distances[node] < cnt_distance:
            continue
        
        for adjacency_node, distance in graph[node]:
            cal_distance = distances[node] + distance
            
            if cal_distance < distances[adjacency_node]:
                distances[adjacency_node] = cal_distance
                heapq.heappush(q, (cal_distance, adjacency_node))
                
    return distances
