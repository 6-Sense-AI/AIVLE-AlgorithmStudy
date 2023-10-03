


## T의 위치에서 맵 끝까지 상하좌우 다 훑음
## 장애물 있으면 멈춤

from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
graph = [list(input().split()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
check = False

def bfs():
    visited = [[False]*n for _ in range(n)]

    ## 선생님 위치 저장
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'T':
                queue.append((i,j))

    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            temp_x, temp_y = x,y

            while True:
                nx = temp_x + dx[i]
                ny = temp_y + dy[i]


                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 'X' and visited[nx][ny] == False:
                        visited[nx][ny] = True
                    elif graph[nx][ny] == 'S':
                        return False
                    elif graph[nx][ny] == 'O':
                        break
                    temp_x, temp_y = nx,ny
                else:
                    break
    return True

def hidden(index):
    global check
    if index == 3:
        if bfs():
            check = True
        return
        
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                hidden(index+1)
                graph[i][j] = 'X'

hidden(0)
if check:
    print("YES")
else:
    print("NO")