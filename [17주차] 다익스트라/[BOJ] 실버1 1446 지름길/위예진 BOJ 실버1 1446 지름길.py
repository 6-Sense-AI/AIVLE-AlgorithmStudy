import sys
input = sys.stdin.readline
import heapq


# n: 지름길의 수, d: 고속도로의 길이
n, l = map(int, input().split())
graph = list([(i+1, 1)] for i in range(l + 1))    # 각 노드의 (연결 노드, 비용) 정보
graph[l] = []
for _ in range(n):
    s, e, cost = map(int, input().split())    # (시작, 도착, 비용)
    if e > l or (e - s) < cost:     # 도로의 길이를 넘어가는 경우, 무시
        continue
    graph[s].append((e, cost))

dist = list(1e9 for i in range(l + 1))    # 각 노드까지의 최단거리 그래프

def dijkstra(start):
    # 시작 초기화
    q = []    # 순회 리스트(최단 거리 기준으로 정렬되는 최소힙)
    heapq.heappush(q, (0, start))    # 최소힙이므로 비용 먼저
    dist[start] = 0
    
    while q:    # 꺼낼 값이 남아있는 동안에 반복
        # 가장 최단거리 정보 꺼내기
        d, now = heapq.heappop(q)

        # 이미 처리된 노드이면, 넘어가기
        if dist[now] < d:
            continue

        # 현재 노드와 인접한 노드들 확인
        for node in graph[now]:
            cost = d + node[1]
            if cost < dist[node[0]]:   # 현재 노드를 거치는 경로가 더 짧은 경우
                dist[node[0]] = cost    # 최단 거리 갱신
                heapq.heappush(q, (cost, node[0]))    # 순회 리스트에 넣어주기

dijkstra(0)
print(dist[l])