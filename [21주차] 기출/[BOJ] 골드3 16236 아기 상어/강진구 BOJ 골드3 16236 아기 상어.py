import sys
from collections import deque

input = sys.stdin.readline
# 미완
# 우선순위 위쪽, 왼쪽
# 몇개를 잡아먹을수 있는지 물고기를 자기 크기 개수만큼 먹을때마다 1씩 커짐
# 한칸 이동시 1초 듬

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

def search_target(shark, graph):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] <= shark:
                cnt += 1
    return cnt


def bfs(graph, start):
    row, col = start
    if graph[row][col] != 0:
        graph[row][col] == 0

    dr = [0, -1, 1, 0]
    dc = [-1, 0, 0 ,1]

    que = deque([(row, col)])
    shark = 2
    time = 0
    # 타겟이 있는지를 알수 있어야하고 없다면 멈추는기능이 필요함

    while que:
        r,c  = que.popleft()
        if search_target(shark, graph) == 0:
            break

        flag = 0
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            if 0<=nr<n and 0<=nc<n and graph[nr][nc] <= shark:
                que.append((nr, nc))
                graph[nr][nc] = 0
                time += 1
                if flag < shark:
                    flag += 1
                else:
                    shark += 1
                    flag = 0
            else:
                if i == 3:
                    break
    return time

s_row, s_col = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            s_row, s_col = i, j

print(bfs(graph, (s_row,s_col)))