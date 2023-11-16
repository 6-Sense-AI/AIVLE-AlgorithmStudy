from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

# 배열 입력 받기
# 맨 뒤에 '\n'까지 제거하기 위해 .rstrip() 입력
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최단거리는 bfs로 풀기
def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        # 상하좌우 다 돌기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            # nx, ny가 범위를 벗어 났을 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
        
            # nx, ny가 0인 경우
            if graph[nx][ny] == 0:
                continue
        
            # nx, ny가 1인 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    
    return graph[n-1][m-1]

print(bfs(0,0))
