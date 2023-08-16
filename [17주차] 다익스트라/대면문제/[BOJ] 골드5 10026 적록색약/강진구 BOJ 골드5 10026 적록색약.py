import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(input()))

normal = [[False for _ in range(n)] for _ in range(n)]
abnormal = [[False for _ in range(n)] for _ in range(n)]

normal_cnt = 0
abnormal_cnt = 0

def bfs(graph, visit, start, color):
    r,c = start
    visit[r][c] = True
    que = deque([(r,c)])
    cnt = 1
    while que:
        r,c = que.popleft()

        dr = [1,-1,0,0]
        dc = [0,0,1,-1]

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            if 0<=nr<n and 0<=nc<n and visit[nr][nc]==False and graph[nr][nc]==color:
                que.append((nr,nc))
                visit[nr][nc] = True
                cnt += 1
            
            if 0<=nr<n and 0<=nc<n and visit[nr][nc]==False and visit == abnormal:
                if color == 'R' or color == 'G':
                    if graph[nr][nc] == 'R' or graph[nr][nc] == 'G':
                        que.append((nr, nc))
                        visit[nr][nc] = True
                        cnt += 1
                    else:
                        if graph[nr][nc] == color:
                            que.append((nr,nc))
                            visit[nr][nc] = True
                            cnt += 1 
    return cnt

c_lst = []

for i in range(n):
    for j in range(n):
        if normal[i][j] == False and bfs(graph, normal, (i,j), graph[i][j]) != 0:
            normal_cnt += 1
        else:
            continue

print(normal_cnt, end=' ')

for i in range(n):
    for j in range(n):
        if abnormal[i][j] == False and bfs(graph, abnormal, (i,j), graph[i][j]) != 0:
            abnormal_cnt += 1
        else:
            continue

print(abnormal_cnt)