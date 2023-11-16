from collections import deque
import sys
## bfs 구현

## 미로에서는 0으로는 이동할 수 없다.
## 좌우상하 dx로 정의해서 이동시키는 bfs를 살펴보자.

def bfs(maze, visited, n, m):
    
    ## 상하좌우 이동 좌표
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    ## 시작 지점 넣고 방문 처리
    q = deque([(0,0,0)])
    visited[0][0] = True
  
    ## 이동한 좌표가 visited에 없고, n * m 크기 미로 내 범위 있어야 하며 0으로는 이동하면 안된다.
    
    while q:
        x, y, cnt = q.popleft()

        if x ==n-1 and y ==m-1:
              return cnt

        ## 이동한 위치 표현
        nxt_list = []
        for i in range(4):
            x_nxt = x + dx[i]
            y_nxt = y + dy[i]
            if 0<= x_nxt <n and 0 <=y_nxt <m:
                nxt_list.append([x_nxt,y_nxt])
            else:
                continue

        ## 방문 위치 아니라면 큐에 넣고 방문 표시       
        for a, b in nxt_list:
            if not visited[a][b] and maze[a][b] == 1:
                q.append((a, b, cnt+1))
                visited[a][b] = True
                
n, m = map(int, sys.stdin.readline().split())
## 미로 입력받기
## 미로 정보는 m개의 정수가 n줄로 붙어서 주어짐
## 리스트로 받은 다음 각각 분리해서 maze 행렬에 넣자

maze = []

for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().strip())))
    
## 방문 상태 리스트 선언

visited = [[False] * (m+1) for _ in range(n+1)]


print(bfs(maze, visited, n, m)+1)
