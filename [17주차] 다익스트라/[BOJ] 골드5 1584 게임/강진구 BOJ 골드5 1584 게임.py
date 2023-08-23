# 미완
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())

graph = [[0 for _ in range(500)] for _ in range(500)]

for _ in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    if x1>x2 and y1>y2:
        for i in range(x2,x1):
            for j in range(y2,y1):
                graph[i][j] = 1
    elif x1>x2 and y2>y1:
        for i in range(x2,x1):
            for j in range(y1,y2):
                graph[i][j] = 1
    elif x1<x2 and y1>y2:
        for i in range(x1,x2):
            for j in range(y2,y1):
                graph[i][j] = 1
    else:
        for i in range(x1,x2):
            for j in range(y1,y2):
                graph[i][j] = 1
    

m = int(input())

for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    if x1>x2 and y1>y2:
        for i in range(x2,x1):
            for j in range(y2,y1):
                graph[i][j] = 2
    elif x1>x2 and y2>y1:
        for i in range(x2,x1):
            for j in range(y1,y2):
                graph[i][j] = 2
    elif x1<x2 and y1>y2:
        for i in range(x1,x2):
            for j in range(y2,y1):
                graph[i][j] = 2
    else:
        for i in range(x1,x2):
            for j in range(y1,y2):
                graph[i][j] = 2
    

visit = [[False for _ in range(500)] for _ in range(500)]

def dfs(graph, visit, start):
    r,c  = start
    visit[r][c] = True
    cnt = 0
    if r==499 and c==499:
        return cnt
    
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        if 0<=nr<500 and 0<=nc<500 and visit[nr][nc]==False:
            if graph[nr][nc] != 2:
                if graph[nr][nc] == 1:
                    cnt += 1
                dfs(graph, visit, (nr,nc))
        
        if i==3 and graph[nr][nc] == 2:
            return -1

            
    return cnt

cnt = dfs(graph, visit, (0,0))

print(cnt)
print(visit[-1][-1])