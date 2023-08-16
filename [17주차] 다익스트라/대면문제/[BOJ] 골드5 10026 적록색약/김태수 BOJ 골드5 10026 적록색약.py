# 런타임 에러,,
# 배열을 따로 만들지 말고 하나로 해보자!!

import sys
input = sys.stdin.readline

# 4방면으로 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 열 입력받기
n = int(input())

# graph_1 = 일반사람을 위한 배열
graph_1 = [0 for _ in range(n)]
visited_1 = [[False] * n for _ in range(n)]

for i in range(n):
    graph_1[i] = list(input().strip())

# graph_2 = 적록색약을 위한 배열
graph_2 = [0 for _ in range(n)]
visited_2 = [[False] * n for _ in range(n)]    

for i in range(n):
    graph_2[i] = []
    for j in graph_1[i]:
        if j == 'G':
            graph_2[i].append('R')
        else:
            graph_2[i].append(j)

# 일반인과 적록색약의 구분
cnt_1 = 0
cnt_2 = 0

# dfs 함수구현
def dfs(x, y, graph, visited):
    visited[x][y] = True
    cur_color = graph[x][y] # cur_color에 현재 색깔을 저장하여 비교
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == False:
                if graph[nx][ny] == cur_color:
                    dfs(nx, ny, graph, visited)


# 일반인으 구역
for i in range(n):
    for j in range(n):
        if visited_1[i][j] == False:
            dfs(i, j, graph_1, visited_1)
            cnt_1 += 1

# 적록색약의 구역
for i in range(n):
    for j in range(n):
        if visited_2[i][j] == False:
            dfs(i, j, graph_2, visited_2)
            cnt_2 += 1

# 답안출력
print(cnt_1, cnt_2)