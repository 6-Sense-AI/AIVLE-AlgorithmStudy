import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]

# 본인보다 크면 X, 같으면 지나가기만, 적으면 먹고 커짐
# 제일 거리가 가까운 곳, IF 많으면 위 -> 왼

# 답 안나옴 ㅜㅜ

dist = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9: # 아기상어 위치
            dist.append(i)
            dist.append(j)

ans = 0 # 도움을 요청할때까지의 초

dx = [-1, 0, 0, 1] # 상좌우하
dy = [0, -1, 1, 0]

def dfs(x, y):
    visited = [[0]*n for _ in range(n)]
    q = deque([[x,y]])
    t = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx and nx < n and 0 <= ny and ny < n and visited[nx][ny] == 0 :
                if arr[x][y] > arr[nx][ny] and arr[nx][ny] != 0:
                    visited[nx][ny] = visited[x][y] + 1
                    t.append((visited[nx][ny] - 1, nx, ny))
                elif arr[x][y] == arr[nx][ny]:
                    visited[nx][ny] =  visited[x][y] + 1
                    q.append([nx,ny])
                elif arr[nx][ny] == 0:
                    visited[nx][ny] =  visited[x][y] + 1
                    q.append([nx,ny])

    return sorted(t, key = lambda x: (x[0], x[1], x[2])) # 식 봄 우선순위 세우는 람다식이란다.


x, y = dist
shark = [2, 0] # 상어 크기
while 1:
    arr[x][y] = dist[0]

    temp = dfs(x,y)

    if not temp: break

    step, xx, yy = temp
    ans += step

    if shark[0] == shark[1] :
        shark[0] += 1
        shark[1] = 0

    arr[x][y] = 0
    x, y = xx, yy


print(ans)