import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

indegree = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

ans = []

q = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    ans.append(now)

    for g in graph[now]:
        indegree[g] -= 1
        if indegree[g] == 0:
            q.append(g)

for a in ans:
    print(a, end=' ')


