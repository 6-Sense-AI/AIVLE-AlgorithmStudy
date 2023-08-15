from collections import deque

n = int(input())
grp = []

for _ in range(n):
    mp = list(map(int, input().split()))
    grp.append(mp)

visited = [[False] * n for _ in range(n)]

dx = [1, 0] # 우
dy = [0, 1] # 하

def bfs(x, y):
    que = deque()
    que.append([x, y])

    while que:
        x, y = que.popleft()
        mv = grp[x][y] # 움직여야할 거리
        
        if mv == -1: # 만약 -1 칸에 있으면 True 리턴
            return True
        
        for i in range(2):
            nx = x + (dx[i] * mv) # 움직여야할 거리만큼 곱해준다
            ny = y + (dy[i] * mv)
        
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if not visited[nx][ny]: # 방문하지 않았을 경우만
                visited[nx][ny] = True
                que.append((nx, ny))
    

if bfs(0, 0):
    print('HaruHaru')

else:
    print('Hing')

                
            


