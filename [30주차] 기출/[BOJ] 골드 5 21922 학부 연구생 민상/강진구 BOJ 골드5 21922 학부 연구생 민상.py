# 민상아 시간초과가 해결이 안된다..
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 1,2는 바람 진행경로랑 수직이면 멈춤 3,4는 꺽임
que = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 9:
            que.append((i,j))

dr = [0,0,1,-1]
dc = [1,-1,0,0]
visit = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
while que:
    x,y = que.popleft()

    for i in range(4):
        r, c = x, y
        nx, ny = dr[i], dc[i]
        while 0 <= r < n and 0 <= c < m:
            visit[r][c] = 1
            if (graph[r][c] == 1 and nx == 0) or (graph[r][c] == 2 and ny == 0):
                break
            elif graph[r][c] == 3:
                nx, ny = -ny, -nx
            elif graph[r][c] == 4:
                nx, ny = ny, nx
            r += nx
            c += ny

for v in visit:
    cnt += v.count(1)
print(cnt)