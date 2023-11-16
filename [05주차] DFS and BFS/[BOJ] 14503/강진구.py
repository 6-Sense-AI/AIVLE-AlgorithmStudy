import sys

input = sys.stdin.readline

n, m = map(int, input().split())

row, col, d = map(int, input().split())

room = []

for _ in range(n):
    room.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]
cnt = 1
visited[row][col] = 1
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 현재 칸 청소
while True:
    flag = 0
    # 주변 네칸 확인
    for _ in range(4):
        d = (d+3)%4
        nr, nc = row+dr[d], col+dc[d]
        # 4칸 중 청소되지 않은 빈칸 있음
        if (0<=nr<n) and (0<=nc<m) and room[nr][nc] == 0:
            if visited[nr][nc] == 0:
                cnt+=1
                visited[nr][nc] = 1
                row, col = nr, nc
                flag = 1
                break
            
    if flag == 0:   # 4칸 중 빈칸 없음
        if room[row-dr[d]][col-dc[d]] == 1:
            print(cnt)
            break
        else:
            row,col = row-dr[d],col-dc[d]
