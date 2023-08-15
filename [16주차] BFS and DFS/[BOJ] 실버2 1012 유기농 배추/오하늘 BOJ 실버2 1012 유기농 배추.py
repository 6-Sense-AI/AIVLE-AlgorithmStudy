import sys
input = sys.stdin.readline
from collections import deque

# 전략 : 완전탐색 + bfs
t = int(input())

## 헷갈렸던 점 !!!!
# 입력 x,y는 우리가 생각하는 일반 제4사분면이었으나,
# 코딩에서의 x,y축은 달라서 수정하는데 너무 오래걸렸다.

for _ in range(t): #테스트 케이스
    m, n, k = map(int, input().split()) # 배추밭 가로, 세로, 위치의 개수

    # 0으로 깔아두기
    arr = [[0]*m for _ in range(n)]

    # 1로 체크
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    # visited 선언
    visited = [[False]*m for _ in range(n)]
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 정답
    cnt = 0

    # bfs 선언
    def bfs(i,j):
        q = deque()
        q.append((i,j))
        visited[i][j] = True

        while q:
            x, y = q.popleft()
            ## 여기에 큐에서 빼낸 다음에 true를 방문표시를 하면 시간초과 남!!!
            # visited[x][y] = True

            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]

                if nx<0 or nx>=n or ny<0 or ny>=m or nx==0 and ny==0:
                    continue
                if arr[nx][ny] == 0: # 그래프가 0이거나 방문했으면
                    continue
                if visited[nx][ny]:
                    continue
                if arr[nx][ny] == 1 and visited[nx][ny] == False: # 그래프가 있는 경우
                    q.append((nx,ny))
                    visited[nx][ny] = True ##여기에 넣어줄때 true를 선언해주어야함!

    # 완전탐색
    for i in range(n): # 세로
        for j in range(m): # 가로
            if arr[i][j] == 1 and visited[i][j] == False: # 1이고 false 면
                bfs(i,j)
                cnt += 1
    print(cnt)