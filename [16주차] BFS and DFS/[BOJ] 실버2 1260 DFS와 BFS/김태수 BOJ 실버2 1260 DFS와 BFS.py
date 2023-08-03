from collections import deque
import sys
input = sys.stdin.readline

# 정점의 개수, 간선의 개수, 시작 정점 입력받기
n, m, v = map(int, input().split())
# 그래프 선언
graph = [[] for _ in range(n+1)]
# 그래프 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 구현
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# BFS 구현
def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# for row in range(n + 1):
#     graph[row].sort()

# 그래프 정렬
for i in graph:
    i.sort()

# 방문노드 
visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)