# deque 잘쓰고싶다..
from collections import deque
import sys
input = sys.stdin.readline

# 입력받기
n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

l = int(input())
rotation = {}
for i in range(l):
    c, d = input().split()
    rotation[int(c)] = d

# 시계방향 - 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀 초기위치, 방향 초기
x, y, d = 0, 0, 0 

snake = deque([])
time = 0
while True:
    snake.append((x,y))
    time += 1

    x += dx[d]
    y += dy[d]

    # 벽에 부딪히거나 자기 몸에 부딪히면
    if x<0 or x>=n or y<0 or y>=n or graph[x][y]==2:
        break

    # 벽이 아니면
    # 사과가 없다면
    if not graph[x][y]:
        i, j = snake.popleft()
        graph[i][j] = 0

    graph[x][y] = 2

    if time in rotation:
        # 만약 시계방향으로 돈다면
        if rotation[time] == 'D':
            d = (d+1) % 4
        else:
            d = (d-1) % 4

print(time)