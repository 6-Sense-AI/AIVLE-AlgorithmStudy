# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

n, m, v= map(int, input().split()) # 정점 개수, 간선 개수, 시작 정점
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

    
def dfs(visited, v, graph):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(visited, i, graph)
            
def bfs(visited, start, graph):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
            
dfs(visited, v, graph)
visited = [False] * (n+1)
print()
bfs(visited, v, graph)
