import heapq
import sys
input = sys.stdin.readline
INF = (1e9) 

# 입력받기
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 쌍방향으로 그래프 연결
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 기본적인 다익스트라 함수
# 최단거리 행렬을 return 한다.
def dijstra(start):
    distance = [INF] * (n+1)
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

    return distance


# 꼭 지나야하는 두 정점 입력받기
v1, v2 = map(int, input().split())

# 블로그 참조...
# 각 정점에서 시작하는 다익스트라
original = dijstra(1)
v1_distance = dijstra(v1)
v2_distance = dijstra(v2)

# 거리계산하기
v1_path = original[v1] + v1_distance[v2] + v2_distance[n]
v2_path = original[v2] + v2_distance[v1] + v1_distance[n]

# 최솟값을 답으로 추출
result = min(v1_path, v2_path)
print(result if result < INF else -1)