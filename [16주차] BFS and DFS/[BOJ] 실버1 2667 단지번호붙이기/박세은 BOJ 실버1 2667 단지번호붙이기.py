from collections import deque

n = int(input())
grp = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
groups = []

dx = [-1, 1, 0, 0]
dy = [-0, 0, -1, 1]

def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = True
    
    cnt = 1

    while que:

        qx, qy = que.popleft()

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny] and grp[nx][ny] == 1:
                cnt += 1
                que.append((nx, ny))
                visited[nx][ny] = True
                
    return(cnt)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grp[i][j] == 1:
            groups.append(bfs(i, j))
            
groups.sort()

print(len(groups))

for i in groups:
    print(i)












