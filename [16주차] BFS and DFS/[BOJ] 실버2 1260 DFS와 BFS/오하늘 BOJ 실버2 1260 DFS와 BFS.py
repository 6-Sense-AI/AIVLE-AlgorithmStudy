import sys
from collections import deque # BFS를 위한 데큐 선언

input = sys.stdin.readline

n, m, v = map(int,input().split()) # 정점, 간선, 시작 정점
graph = [[] for _ in range(n+1)] # 그래프 선언
visited = [False] * (n+1) # 정점 + 1

# 그래프 탐색 _ 양방향
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort() # 정렬
    graph[b].sort()

# dfs
def dfs(visited, v, graph):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(visited, i, graph)

# bfs
def bfs(visited, v, graph):
    q = deque([v])
    visited[v] = True

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
dfs(visited, v, graph)
visited = [False] * (n+1) # 초기화
print()
bfs(visited, v, graph)
