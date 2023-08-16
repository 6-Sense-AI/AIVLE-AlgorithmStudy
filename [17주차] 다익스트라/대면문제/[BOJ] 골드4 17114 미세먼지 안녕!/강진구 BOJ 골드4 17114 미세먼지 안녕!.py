'''
1초동안 순서대로 일어남

미세먼지 확산
인접한 네방향으로 확산
공기청정기 있거나, 칸이 없으면 확산은 없음
확산 양 graph[r][c]//5
확산 후 graph[r][c] -= (graph[r][c]//5) * (확산 방향 수)

공기청정기 작동
공기청정기 바람
위쪽은 반시계 순환, 아래쪽은 시계방향 순환
바람 불면 미세먼지가 바람의 방향대로 한 칸씩 이동
공기청정기로 들어가면 미세먼지 모두 정화, 바람 불면 미세먼지 사라짐
'''

import sys
from collections import deque

input = sys.stdin.readline

r,c,t = map(int, input().split())

graph = []

for _ in range(r):
    graph.append(list(map(int, input().split())))

clean = []

for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            clean.append((i,j))

# 미세먼지 확산
def diffusion(graph, clean):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    for row in range(r):
        for col in range(c):
            if graph[row][col] != -1:
                x = graph[row][col]
            else:
                continue
            flag = 0
            for i in range(4):
                nr = row+dr[i]
                nc = col+dc[i]

                if 0<=nr<r and 0<=nc<c and (nr,nc) not in clean:
                    graph[nr][nc] += x//5
                    flag += 1
            
            graph[row][col] -= (x//5) * flag
    return graph

# 공기청정기 작동
def cleaner(graph, clean):
    ur,uc = clean[0]
    dwr,dwc = clean[1]

    # 위쪽 순환
    que = deque(graph[ur][1:])
    que.appendleft(0)
    que.appendleft(-1)
    x = que.pop()

    graph[ur] = list(que)

    for i in range(ur-1,-1,-1):
        y = graph[i][c-1]
        graph[i][c-1] = x
        x = y
    
    for i in range(c-2,-1,-1):
        y = graph[0][i]
        graph[0][i] = x
        x = y
    
    for i in range(1,ur):
        y = graph[i][0]
        graph[i][0] = x
        x = y
    
    # 아래쪽 순환
    que = deque(graph[dwr][1:])
    que.appendleft(0)
    que.appendleft(-1)
    x = que.pop()

    graph[dwr] = list(que)

    for i in range(dwr,r):
        y = graph[i][c-1]
        graph[i][c-1] = x
        x = y
    
    for i in range(c-2,-1,-1):
        y = graph[r-1][i]
        graph[r-1][i] = x
        x = y
    
    for i in range(r-2,dwr,-1):
        y = graph[i][0]
        graph[i][0] = x
        x = y
    return graph

for _ in range(t):
    graph = diffusion(graph, clean)
    graph = cleaner(graph,clean)

s = 0

for g in graph:
    if -1 not in g:
        s += sum(g)
    else:
        s += sum(g)+1
    
print(s)
