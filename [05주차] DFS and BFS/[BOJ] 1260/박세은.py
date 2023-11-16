import sys
from collections import deque

def dfs(gph, vv, visited):
    visited[vv] = True
    print(vv, end = ' ')
    
    for i in gph[vv]:
        if not visited[i]:
            dfs(gph, i, visited)
  
            
def bfs(gph, s, visited):
    queue = deque([s])
    
    visited[s] = True
    
    while queue:
        vv = queue.popleft()
        print(vv, end=' ')
        
        for i in gph[vv]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, sys.stdin.readline().split())
gph = []

for _ in range(m):
    gph.append(list(map(int, input().split())))
    
visited = [False] * m
     
print(dfs(gph, v, visited))
print(bfs(gph, v, visited))
