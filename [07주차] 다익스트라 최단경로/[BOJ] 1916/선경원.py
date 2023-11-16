import heapq
import sys

## 입력받기
n = int(sys.stdin.readline()) ## 도시 개수
m = int(sys.stdin.readline()) ## 버스 개수
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int,sys.stdin.readline().split()) ## 승차 도시, 하차 도시, 비용
    graph[a].append((b,c))

start, end = map(int, sys.stdin.readline().split()) ## 시작 도시, 목표 도시

INF = int(10e9)

distance = [INF]*(n+1)


def min_cost(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        ## 직선 이동이 더 작은 비용이면 패스
        if distance[now] < dist:
            continue

        ## 직선 이동과 경유 이동 비교해서 갱신
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost

                ## q에 cost와 하차 도시 추가
                heapq.heappush(q,(cost,i[0]))

min_cost(start)
print(distance[end])
