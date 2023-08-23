# 노력의 흔적...
# △△△
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dijstra(start):
    q = []
    # 그래프 시작점과 x, y 좌표
    heapq.heappush(0, graph[0][0], 0, 0)
    distance[0][0] = 0

    while q:
        now, x, y = heapq.heappop(q)
        
        if nx == n-1 and ny == n-1:
            # 결과문
            break
        
        # 좌표이동하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n) and (0<=ny<n):
                next = now + graph[nx][ny]
            



# 입력
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[] * n for i in range(n+1)]