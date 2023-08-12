
## 가로와 세로의 칸 수가 같은 정사각형의 구역 내부

## 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸

## ‘쩰리’가 이동 가능한 방향은 오른쪽과 아래 뿐

## 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼

## 게임판의 승리 지점(오른쪽 맨 아래 칸)에는 -1이 쓰여 있음

from collections import deque


## 오른쪽과 아래 이동만 가능
dx = [1,0]
dy = [0,1]


def bfs(x, y):
    queue = deque()
    queue.append([x,y])


    while queue:
        x, y = queue.popleft()

        if graph[x][y] == -1:
            return True
        for i in range(2):
            nx = x + dx[i]*graph[x][y]
            ny = y + dy[i]*graph[x][y]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx,ny])

                
## 맵 크기 입력 n * n 맵

n = int(input())  

graph = [list(map(int, input().split())) for _ in range(n)]
    
           
visited = [[False]*3 for _ in range(n)]
        
if bfs(0,0):
    print("HaruHaru")

else:
    print("Hing")


