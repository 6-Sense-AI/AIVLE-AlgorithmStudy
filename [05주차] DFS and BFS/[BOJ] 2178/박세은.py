import sys
from collections import deque

input = sys.stdin.readline

# 행, 열 갯수 입력
n, m = map(int, input().split())

grp = []

# 그래프 그리기
for i in range(n):
    grp.append(list(map(int, input().rstrip())))

# 상, 하, 좌, 우 좌표   
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수
def bfs(x, y):
    que = deque()       # 큐 생성
    que.append((x,y))       # 탐색 시작점 입력
    
    while que:      # 큐가 빌때까지 반복
        x, y = que.popleft()        # 제일 먼저 들어온 큐 반환?
    
        for j in range(4) :     # 상하좌우 탐색
        
            nx = x + dx[j]      # 상, 하 nx에 저장
            ny = y + dy[j]      # 좌, 우 ny에 저장
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m :     # 값이 범위를 넘는 경우 무시
                continue
            
            if grp[nx][ny] == 0:        # 벽을 만난 경우 무시
                continue
            
            if grp[nx][ny] == 1:        
                grp[nx][ny] = grp[x][y] + 1     # 노드 방문시 거리 기록
                que.append((nx, ny))
                
    return grp[n - 1][m - 1]        # 도착지점 거리 반환
        
print(bfs(0,0))
