## 아직 다 못풀었음

from collections import deque

# 구역 표시하기
grp = [[0 for _ in range(501)] for _ in range(501)]  # 우선 안전구역만으로 이뤄진 그래프 그리기

n = int(input())  # 위험한 구역의 수

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            grp[i][j] = 1

m = int(input())  # 죽음의 구역의 수

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            grp[i][j] = -1

# 최단거리 구하기
life = 0  # 잃은 생명력
visited = [[False for _ in range(501)] for _ in range(501)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global life

    que = [(x, y)]

    while que:
        x, y = que.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx > 501 or nx < 0 or ny > 501 or ny < 0:
                continue

            dead = 0  # 사망구역
            cost = life + grp[nx][ny]

            if cost > life and visited[nx][ny] == False:
                visited[nx][ny] = True
                continue

            if cost == life and visited[nx][ny] == False:
                visited[nx][ny] = True
                life = cost
                que.append((nx, ny))

            if cost < life and visited[nx][ny] == False:
                visited[nx][ny] = True
                dead = -1
                continue


bfs(0, 0)
print(life)
