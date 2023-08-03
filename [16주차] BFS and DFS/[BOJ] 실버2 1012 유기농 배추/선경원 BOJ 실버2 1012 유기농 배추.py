
## [BOJ] 1012 유기농 배추


## 지렁이는 상하좌우 이동 가능

## 0 : 배추 없는 땅, 1 : 배추 있는 땅




## 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사

## 배추가 있는 위치에서 인접 배추만 bfs로 조져보자

from collections import  deque

## 상하좌우 이동
dx = [0,0,1,-1]
dy = [1,-1,0,0]



## 지렁이가 거쳐가면 그 부분은 0으로 바꿔준다(먹어치우는 게 아니라 이미 보호받은 구역이라는 뜻)

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            ## 지렁이가 이동한 곳에 배추 있으면
            ## 보호완료 표시 해주고 queue에 해당 위치 추가

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    



T = int(input()) ## 테스트 케이스

for i in range(T):
    cnt = 0
    n, m, k = map(int,input().split())

    ## 빈 땅 입력
    graph = [[0]*m for _ in range(n)]  

    ## 배추 위치 입력
    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt+=1

    print(cnt)