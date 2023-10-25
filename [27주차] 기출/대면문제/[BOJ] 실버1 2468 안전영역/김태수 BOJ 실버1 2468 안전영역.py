import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def func(x, y, visited, h):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <0 or nx>=n or ny<0 or ny>=n:
            continue
        if not visited[nx][ny] and graph[nx][ny] > h:
            func(nx,ny,visited, h)

count = []
for h in range(101):
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                func(i, j, visited, h)
                cnt += 1
    count.append(cnt)

print(max(count))