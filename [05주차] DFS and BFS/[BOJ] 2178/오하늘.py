# 미로 탐색
import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split()) # x y

graph = [list(map(int, input().strip())) for _ in range(n)] # 세로, n

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    
    while q:
        if graph[n-1][m-1]>1:
            print(graph[n-1][m-1])
            break
        x, y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx <0 or nx>=n or ny <0 or ny>=m or nx==0 and ny==0:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))
            
bfs(0,0)
