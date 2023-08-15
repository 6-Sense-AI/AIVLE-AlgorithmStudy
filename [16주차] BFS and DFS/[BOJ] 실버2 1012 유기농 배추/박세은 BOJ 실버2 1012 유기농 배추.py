from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    ### que = deque((x, y)) 로 쓰고 line 12 실행하면 값을 받아오면서 에러 발생
    que = [(x, y)]
    grp[x][y] = 0

    while que:
        x, y = que.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if grp[nx][ny] == 1:
                que.append((nx, ny))
                grp[nx][ny] = 0

                
t = int(input()) # 테스트 케이스 수

for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    grp = [[0] * (n) for _ in range(m)] # 밭의 크기만큼 그래프 생성

    for _ in range(k):
        a, b = map(int, input().split())
        grp[a][b] = 1 # 배추 심어주기
    
    cnt = 0 # 지렁이

    for i in range(m):
        for j in range(n):
            if grp[i][j] == 1:
                bfs(i, j)
                cnt += 1
    
    print(cnt)




