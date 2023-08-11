import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)

for _ in range(int(input())):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n)]

def bfs(graph, visited, start):
    visited[start-1] = True
    que = deque([start])
    cnt = 0

    while que:
        x = que.popleft()
        for g in graph[x]:
            if visited[g-1] == False:
                que.append(g)
                visited[g-1] = True
                cnt += 1
    
    return cnt


print(bfs(graph, visited, 1))
