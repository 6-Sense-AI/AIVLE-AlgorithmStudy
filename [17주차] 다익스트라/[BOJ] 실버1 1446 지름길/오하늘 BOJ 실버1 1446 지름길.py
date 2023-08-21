# 다익스트라 기본 코드
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한

n,m = map(int, input().split()) # 지름길 개수, 최종 거리
g = [[] for i in range(m+1)] # 그래프
distance = [INF] * (m+1) # 최단 거리 테이블 초기화

for i in range(m): # 그냥 정루트로 걸어가는 거리
    g[i].append((i+1,1)) # 각 1로 값을 줌

# 지름길
for _ in range(n):
    a,b,c =  map(int, input().split()) # a번 노드에서 b번 노드 가는 비용 c
    if b > m: # 역주행
        continue
    g[a].append((b,c))

import heapq
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start)) # 처음에는 거리0이고 시작노드 넣어줌
    distance[start] = 0 # 시작노드는 거리가 0이니까

    while q:
        dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(작은거리)

        # 이미 처리된 노드
        if distance[now] < dist: #이미 입력되어있는 값이 현재노드까지의 거리보다 작으면 이미 방문
            continue # 다음으로 넘어감

        # 현재 노드와 연결된 다른 노드들 확인
        for i in g[now]: # 노드, 비용 // i[0], i[1]
            # cost = dist + i[1] # 비용 = 거리 + 값

            if dist + i[1] < distance[i[0]]: # 현재 노드를 거치면 이동거리가 더 짧은 경우
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))

# 다익스트라 수행
dijkstra(0)
print(distance[m])
