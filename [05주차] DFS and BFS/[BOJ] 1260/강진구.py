import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

n,m,v = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

for k in graph.keys():
    graph[k].sort()

def dfs(graph, visited_dfs, v):
    visited_dfs[v] = True
    
    print(v, end=' ')
    for g in graph[v]:
        if not visited_dfs[g]:
            dfs(graph,visited_dfs,g) 
    
def bfs(graph, visited_bfs, v):
    que = deque([v])
    visited_bfs[v] = True
    
    while que:
        x = que.popleft()
        print(x, end=' ')
        
        for g in graph[x]:
            if not visited_bfs[g]:
                que.append(g)
                visited_bfs[g] = True

dfs(graph, visited_dfs, v)
print()
bfs(graph, visited_bfs, v)


