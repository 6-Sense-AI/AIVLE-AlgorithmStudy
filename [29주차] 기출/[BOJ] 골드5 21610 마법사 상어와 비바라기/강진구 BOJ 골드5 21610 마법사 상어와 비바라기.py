import sys
from collections import deque
# cloud도 deque로 해야 시간초과가 안걸림

input = sys.stdin.readline

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

ds = [list(map(int, input().split())) for _ in range(m)]

D = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

que = deque(ds)

cloud = deque([[n-1,0],[n-1,1],[n-2,0],[n-2,1]])

while que:
    d,s = que.popleft()
    # 구름위치 변화
    for c in cloud:
        c[0] = (c[0] + D[d-1][0]*s)%n
        c[1] = (c[1] + D[d-1][1]*s)%n
        
    for c in cloud:
        board[c[0]][c[1]] += 1

    
    for c in cloud:    
        cnt = 0
        for i in range(1,8,2):
            nr = c[0] + D[i][0]
            nc = c[1] + D[i][1]
            if 0<=nr<n and 0<=nc<n and board[nr][nc]>0:
                cnt += 1
            else:
                continue
        board[c[0]][c[1]] += cnt
    
    last_cloud = cloud
    cloud = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and [i,j] not in last_cloud:
                cloud.append([i,j])
                board[i][j] -= 2
            else:
                continue

water = 0
for i in range(n):
    for j in range(n):
        water += board[i][j]

print(water)