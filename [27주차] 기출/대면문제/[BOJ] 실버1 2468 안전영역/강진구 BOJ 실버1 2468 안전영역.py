import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

visit = [[False for _ in range(n)] for _ in range(n)]

def bfs(graph, start, visit, k):

    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    row,col = start[0],start[1]
    
    que = deque()
    que.append((row,col))
    
    while que:
        r,c = que.popleft()
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            if 0<=nr<n and 0<=nc<n:
                if visit[nr][nc] == False and graph[nr][nc] > k:
                    visit[nr][nc] = True
                    que.append((nr,nc))
                    
count = 0
ans = 0
max_v = 0

for i in range(n):
    for j in range(n):
        max_v = max(max_v, graph[i][j])

for k in range(max_v):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and visit[i][j] == False:
                bfs(graph, (i,j), visit, k)
                count+=1
    
    ans = max(count, ans)
    count = 0
    visit = [[False for _ in range(n)] for _ in range(n)]

print(ans)
