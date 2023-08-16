import sys
input = sys.stdin.readline
from collections import deque
import copy

# 적록색약은 빨강과 초록 같은 취급

n = int(input())
arr1 = [list(input().strip()) for _ in range(n)]
arr2 = copy.deepcopy(arr1)
for i in range(n):
    for j in range(n):
        if arr2[i][j] == 'G':
            arr2[i][j] = 'R'

p1visited = [[False]*n for _ in range(n)]
p2visited = [[False]*n for _ in range(n)]

p1cnt = 0 # 일반사람
p2cnt = 0 # 적록색약

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(arr,visited,x,y,target,p):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n or nx==0 and ny==0:
                continue
            # if p == 'p1':
                # if arr[nx][ny] != target:
                #     continue
            # if p == 'p2':
            #     if arr[nx][ny] == 'G': # 초록을 RED 취급
            #         arr[nx][ny] = 'R'
            if arr[nx][ny] != target:
                continue
            if not visited[nx][ny] :
                q.append((nx,ny))
                visited[nx][ny] = True


for i in range(n): # i 세로 x
    for j in range(n): # j 가로 y
        if not p1visited[j][i] :
            bfs(arr1,p1visited,j,i,arr1[j][i],'p1')
            p1cnt += 1
        if not p2visited[j][i] :
            bfs(arr2,p2visited,j,i,arr2[j][i],'p2')
            p2cnt += 1

print(p1cnt, p2cnt)