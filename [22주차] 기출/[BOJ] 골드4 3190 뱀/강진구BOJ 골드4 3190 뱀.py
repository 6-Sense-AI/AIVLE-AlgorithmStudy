import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

k = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

board[0][0] = 2

for _ in range(k):
    r,c = map(int, input().split())
    board[r-1][c-1] = 1

rotation = deque([])

l = int(input())

for _ in range(l):
    x, d = input().split()
    rotation.append((int(x), d))

dr = [0,1,0,-1]
dc = [1,0,-1,0]

cur_d = 0

cur_r, cur_c = 0,0
tail = deque([(cur_r,cur_c)])
time = 0

while 0<=cur_r<n and 0<=cur_c<n:
    if rotation:
        x,d = rotation.popleft()

        if time == x:
            if d == 'D':
                if cur_d < 3:
                    cur_d += 1
                else:
                    cur_d = 0
            else:
                if cur_d > 0:
                    cur_d -= 1
                else:
                    cur_d = 3
        else:
            rotation.appendleft((x,d))
        
    
    nr = cur_r + dr[cur_d]
    nc = cur_c + dc[cur_d]
    
    if 0<=nr<n and 0<=nc<n:
        pass
    else:
        time+=1
        break
    
    

    if board[nr][nc] == 1:
        board[nr][nc] = 2
        tail.append((nr,nc))
    elif board[nr][nc] == 0:
        board[nr][nc] = 2
        t_r,t_c = tail.popleft()
        board[t_r][t_c] = 0
        tail.append((nr,nc))
        
    else:
        time+=1
        break
    
    cur_r = nr
    cur_c = nc
    time+=1


print(time)