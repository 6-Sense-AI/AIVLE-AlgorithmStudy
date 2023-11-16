from collections import deque

## dfs 구현
def dfs(graph, v, visited):
    # 방문한 노드 표시
    visited[v] = True
    print(v, end = ' ')
    # 다음 노드 방문 안했으면 dfs
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

## bfs 구현
def bfs(graph, v, visited):
    queue = deque([v])
    # 방문 노드 표시
    visited[v] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
    ## graph에서 방문하지 않은 노드 있으면 queue에 넣기
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
     
## 노드 연결 상태 
## graph는 n개 정점에 대한 간선 연결 정보

n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()
    
visited = [False]*(n+1)
dfs(graph,v,visited)
print()    
visited = [False]*(n+1)
bfs(graph,v,visited)

