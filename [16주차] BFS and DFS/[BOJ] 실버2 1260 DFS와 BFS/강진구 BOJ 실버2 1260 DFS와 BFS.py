import sys
from collections import defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,v = map(int, input().split())

graph = defaultdict(list)
visited = [False]*n

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(graph, visited, s, node):
    visited[s-1] = True
    node.append(s)
    for g in sorted(graph[s]):
        if visited[g-1] == False:
            dfs(graph, visited, g, node)
        else:
            continue
    
    if visited:
        return

node = []

dfs(graph, visited, v, node)
print(' '.join(str(n) for n in node))


def bfs(graph, visited, s, node):
    que = deque([])
    que.append(s)
    node.append(s)
    visited[s-1] = True

    while que:
        v = que.popleft()
        
        for g in sorted(graph[v]):
            if visited[g-1]==False:
                que.append(g)
                visited[g-1] = True
                node.append(g)

    return node

node1 = []
visited = [False]*n
n1 = bfs(graph, visited, v, node1)
print(' '.join(str(n) for n in n1))