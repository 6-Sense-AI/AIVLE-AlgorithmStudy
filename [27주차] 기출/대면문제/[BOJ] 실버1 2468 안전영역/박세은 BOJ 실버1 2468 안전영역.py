from collections import deque
import copy

n = int(input())
grp = []
ste = [[True] * n for _ in range(n)] 
tst = []

for _ in range(n):
    m = list(map(int, input().split()))
    grp.append(m)

    for i in m:
        if i not in tst:
            tst.append(i)

tst.sort()
tst = deque(tst)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mx = 0

def bfs(x, y):
    tmx = 0

    que = deque()
    que.append([x, y])
    ste_cy = copy.deepcopy(ste)
    ste_cy[x][y] = False

    while que:     
        x, y = que.popleft()
        ec = False

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and ste_cy[nx][ny] == True:
                if ste[nx][ny] == True:
                    que.append([nx, ny])
                    ec = True
                
                else: ste_cy[nx][ny] = False
            
        if ec:
            tmx += 1
        
    return tmx

while tst:
    dng = tst.popleft()

    for i in range(n):
        for j in range(n):
            if grp[i][j] <= dng:
                ste[i][j] = False
            
            else:
                idx = [i, j]
                if ste[idx[0]][idx[1]]:
                    mx = max(mx, bfs(idx[0], idx[1]))
                    ste[idx[0]][idx[1]] = False


print(mx)



