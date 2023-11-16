# 1번에서 N번으로 이동, 양방향 이동 가능

import sys, heapq
input = sys.stdin.readline

# 입력 받기
n, e = map(int, input().split())    # n: 노드 수, e: 간선 수
graph = [[] for _ in range(n +  1)]    # 그래프 비용 정보 저장
for _ in range(e):
    n1, n2, c = map(int, input().split())
    graph[n1].append((n2, c))    # 양방향 연결 저장
    graph[n2].append((n1, c))
v1, v2 = map(int, input().split())    # v1, v2: 반드시 들러야 하는 2개의 노드

# 초기 설정
INF = int(1e9)    # 무한대 설정
distance = [INF] * (n + 1)    # 현재까지의 최단 경로 저장 리스트

# 최단경로 함수 생성 (시작 위치, 도착 위치, 최단 경로 저장 테이블)
def dijkstra(start, distance):
    
    # distance 테이블 초기화
    distance = [INF] * len(distance)
    
    # 먼저 시작 노드를 최소힙에 넣기
    q = []
    heapq.heappush(q, (0, start))    # 적은 비용 순서대로 출력하기 위해, (비용, 노드) 순서대로 넣기
    distance[start] = 0    # 자기 자신으로의 비용은 0

    while q:
        dist, now = heapq.heappop(q)    # 최소힙에서 가장 비용 적은 것 꺼내기
        if distance[now] < dist:    # 방문한 곳이면, 넘어가기
            continue
        
        # 인접 노드 모두 확인
        for n, c in graph[now]:
            cost = dist + c
            if cost < distance[n]:    # 현재 노드를 거쳐서 가는 비용이 더 적다면,
                distance[n] = cost    # distance 테이블 갱신,
                heapq.heappush(q, (cost, n))    # 최소힙에 넣어주기
    return distance
        
start = 1    # 우리의 목표는 1에서 시작, n에 도착 
cs = dijkstra(start, distance)    # start지점에서 모든 경로로의 최단경로 구함
c1= dijkstra(v1, distance)    # v1에서 모든 경로로의 최단경로
c2 = dijkstra(v2, distance)    # v2에서 모든 경로로의 최단경로

# (s->v1->v2->e) / (s->v2->v1->e) 둘 중에 최단 경로 출력
res = min(cs[v1] + c1[v2] + c2[n], cs[v2] + c2[v1] + c1[n])

# 결과 출력
# 불가능한 경로라면, -1 출력
print(res) if res < INF else print(-1)