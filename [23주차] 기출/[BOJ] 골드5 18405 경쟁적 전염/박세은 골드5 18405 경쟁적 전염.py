from collections import deque

n, k = map(int, input().split())
grp = []
virus = []

for i in range(n):
    g = list(map(int, input().split()))
    grp.append(g)

    for j in range(n):
        if grp[i][j] != 0:
            virus.append((grp[i][j], i, j))

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, x, y):
    que = deque(virus)
    cnt = 0
    while que:
        if cnt == s:
            break

        for _ in range(len(que)):
            num, x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if grp[nx][ny] == 0:
                        grp[nx][ny] = grp[x][y]
                        que.append((grp[nx][ny], nx, ny))
        
        cnt += 1

virus.sort()
bfs(s,x,y)
print(grp[x-1][y-1])



