import sys

input = sys.stdin.readline

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

visit = [[0 for _ in range(m)] for _ in range(n)]

v = 0
cnt = 0

def dfs(start, visit, board, cnt):
    row, col = start
    visit[row][col] = 1
    global v
    
    v += board[row][col]
    
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if cnt < 4:
            if 0<=nr<n and 0<=nc<m and visit[nr][nc] == 0:
                visit[nr][nc] = 1
                dfs((nr,nc), visit, board, cnt+1)
        else:
            return 
            # v를 초기화 하고 맥스값을 비교할 필요가 잇음


mv = max(map(max,board))

for i in range(n):
    for j in range(m):
        dfs((i,j), visit, board, cnt)
        
        mv = max(mv,v)
        v = 0
        cnt = 0
        visit[i][j] = 0

print(mv)