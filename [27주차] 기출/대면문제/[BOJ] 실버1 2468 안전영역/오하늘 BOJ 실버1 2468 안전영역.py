import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) #칸 수
g = [list(map(int, input().split())) for i in range(n)]

# 여기서 max(max)를 하게 되면 오류남. 이유는 밑의 링크 참고
# https://www.acmicpc.net/board/view/123423
# max_st = max(max(g))

max_st = 0
max_st = max(max_st, max(g[-1]))

ans = [1]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,st,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True # 시작 방문처리

    while q:
        x,y = q.popleft()

        flag = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny < 0 or ny>=n or nx == 0 and ny == 0:
                continue
            if g[nx][ny] <= st: # 기준보다 낮고
                continue
            if visited[nx][ny] == True: # 이미 방문
                continue
            else :
                visited[nx][ny] = True
                q.append((nx,ny))
                flag = 1
            if i == 3 and flag == 0: # 사방이 막힘
                return
            
for i in range(max_st): # 기준
    visited = [[False]*n for i in range(n)]
    cnt = 0
    for k in range(n): # 그래프 하나씩 돌아
        for j in range(n):
            if visited[k][j] == False and g[k][j] > i:
                bfs(k,j,i,visited)
                cnt += 1
    ans.append(cnt)

print(max(ans))