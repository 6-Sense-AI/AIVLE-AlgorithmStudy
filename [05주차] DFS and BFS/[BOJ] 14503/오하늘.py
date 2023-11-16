# 로봇 청소기 14503
from collections import deque
n, m = map(int, input().split()) # 세로, 가로
r, c, d = map(int, input().split()) # 처음 로봇 청소기 좌표, 로봇 청소기가 바라 보는 방향
# 0북, 1동, 2남, 3서
graph = [list(map(int, input().split())) for _ in range(n)] # 방의 정보

# 상 우 하 좌 이유는 방향 d = 0 1 2 3 순임 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, d, graph):
    visited = [[0] * m for _ in range(n)] # 청소 유무 리스트
    cnt = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = 1 # 청소

    while q:
        flag = 0
        x, y = q.popleft()
        for i in range(4):
            d = (d+3) % 4 # 반시계 방향으로 90도
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or nx == 0 and ny == 0:
                continue
            if graph[nx][ny] == 1: # 벽
                continue

            # 청소되지 않은 빈 칸이 있는 경우
            if graph[nx][ny] == 0 and visited[nx][ny] == 0 : # 벽 아님, 청소 안 함
                cnt += 1
                q.append((nx, ny))
                visited[nx][ny] = 1 # 청소함
                flag = 1
                break

        # 청소되지 않은 빈 칸이 없는 경우
        if flag == 0:
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            if graph[x-dx[d]][y-dy[d]] == 1:
                print(cnt)
                break
            else :
                # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                q.append((x-dx[d],y-dy[d]))

bfs(r, c, d, graph)
