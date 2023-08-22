import sys
input = sys.stdin.readline
import heapq
INF = (1e9) # 무한대

n, m, x, y = map(int, input().split()) # 이웃집 수, 양방향 도로 수, 하루 제한거리, 성현이집
g = [[] for i in range(n)]
distance = [INF] * (n) # 최단거리 테이블
visited = [False] * (n)
day = 0

for _ in range(m): # 도로
    u, v, w = map(int, input().split())
    g[u].append((v,w))
    g[v].append((u,w))

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


dijkstra(y)

# 여기는 인터넷 참고함 ㅜ.ㅜ
for i in range(n): # 최소거리*2 x이상이면 못감 -1
    if distance[i] > x//2:
        print(-1)
        exit() # 끝

# 최소거리*2의 합 이하인 조합의 최소개수
# 가까운곳부터 방문하므로 정렬
distance.sort()
limit = 0
day = 1
for i in range(n):
    if (limit+distance[i])*2 <= x:
        limit = limit+distance[i]
    else:
        limit = distance[i]
        day+=1
print(day)