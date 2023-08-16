r, c, t = map(int, input().split())
dust = [] # 먼지
fresh = [] # 공기청정기 위치

for _ in range(r):
    d = list(map(int, input().split()))
    dust.append(d)

# 1. 미세먼지 확산
apd = [[0]*c for _ in range(r)] # 확산량 표시해줄 그래프

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def ctrl(i, j):
    cnt = 0
    for t in range(4):
        nx = i + dx[t]
        ny = j + dy[t]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        
        if dust[nx][ny] == -1:
            continue

        apd[nx][ny] = apd[nx][ny] + (dust[i][j] // 5)
        cnt += dust[i][j] // 5

    dust[i][j] = dust[i][j] -  cnt   

for i in range(r):
    for j in range(c):
        if dust[i][j] == -1: # 공기청정기 위치 저장 (2번에서 쓸거임)
            fresh.append((i,j))

        if dust[i][j] == 0: # 먼지가 없으면 넘김
            continue

        if dust[i][j] != -1: # 먼지가 있으면서 공기청정기가 아니라면
            ctrl(i, j)

for q in range(r):
    for j in range(c):
        dust[q][j] += apd[q][j]

# 2. 공기청정기 가동
def up(x, y):
    for i in range(x):
        for j in range(y):
            if dust[i][j] != 0:
                if j-1 >= 0 and i == 0:
                    dust[i][j-1] = dust[i][j]
                    dust[i][j] = 0
                
                if j == y-1 and i > 0 and i-1 >= 0:
                    dust[i-1][j] = dust[i][j]
                    dust[i][j] = 0
                
                if i == x and j+1 < y:
                    dust[i][-1]






